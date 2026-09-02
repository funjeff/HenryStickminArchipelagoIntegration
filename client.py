import asyncio
import time

import os
import Utils
import websockets
import functools
from copy import deepcopy
from typing import List, Any, Iterable
from NetUtils import decode, encode, NetworkItem, NetworkPlayer, ClientStatus
from MultiServer import Endpoint
from CommonClient import CommonContext, gui_enabled, ClientCommandProcessor, logger, get_base_parser
from .henry_to_arc_names import *
from .henryHelpers import *
from pathlib import Path

DEBUG = False

class HenryCommandProcessor(ClientCommandProcessor):
    def _cmd_set_henry_path(self, path:str):
        """Set your henry stickmin save file path nessasary to comunicate with the game"""
        self.ctx.save_path = path
        create_comunication_files(self.ctx)
        logger.info(f"Henry Stickmin Save Path set to " + path)
    
    def _cmd_deathlink(self):
        """Turn on or off deathlink, nothing happens to you when your friends die so feel free to turn this on if you hate them"""
        logger.info(f"Deathlink set to " + str(not self.ctx.deathlink))
        self.ctx.deathlink = not self.ctx.deathlink
    def _cmd_sync_to_henry(self):
        """Syncs your current items to henry stickmin, this is done automatically when you get new items, but you can use this command to force a sync if you think something is wrong"""
        henry_item_names = arc_id_to_henry_input_name(self.ctx.all_known_items)
        henry_item_names = add_vanila_progression_items(self.ctx,henry_item_names)
        henry_item_names = add_phone_a_friend_items(self.ctx,henry_item_names)
        henry_item_names = add_timeline_items(self.ctx,henry_item_names)
        send_items_to_henry(self.ctx, henry_item_names)
        logger.info(f"Synced Items to Henry Stickmin")

class HenryContext(CommonContext):
    game = "The Henry Stickmin Collection"
    save_path = ""
    command_processor = HenryCommandProcessor
    items_handling = 0b111
    henryslotdata = None
    deathlink = False
    all_known_items = []

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            self.henryslotdata = args['slot_data']
            self.locations_checked.update(args['checked_locations'])

        elif cmd == 'ReceivedItems':
            update_henry_input(self,args['items'])

    def run_gui(self):
        from kvui import GameManager

        class HenryManager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago Henry Client"

        self.ui = HenryManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

    async def get_save_path(self):
        # TODO save path so I only have to prompt for it the first time
        if not self.save_path:
            logger.info('Enter the Path to your henry stickmin save files pls')
            self.save_path = await self.console_input()
            create_comunication_files(self)
    
    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(HenryContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect(game="The Henry Stickmin Collection")
        await self.get_save_path()


async def henry_control_loop(ctx: HenryContext):
    try:
        while not ctx.exit_event.is_set():
            try:
                await check_henry_output(ctx)
                        
            except FileNotFoundError:
                values = []

            await asyncio.sleep(0.1)
    except Exception as e:
        logger.exception(e)
        logger.info("Aborting Henry Client due to errors")


def launch(*launch_args: str):
    async def main():
        parser = get_base_parser()
        args = parser.parse_args(launch_args)

        ctx = HenryContext(args.connect, args.password)
        attempt_find_path(ctx)
        
        contol_loop = asyncio.create_task(henry_control_loop(ctx), name="ControlLoop")

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        await contol_loop
        await ctx.exit_event.wait()

    Utils.init_logging("HenryClient")
    # options = Utils.get_options()

    import colorama
    colorama.just_fix_windows_console()
    asyncio.run(main())
    colorama.deinit()


def create_comunication_files(ctx: HenryContext):
    open(os.path.join(ctx.save_path, "archipelagoIn.sav"), "a").close()
    open(os.path.join(ctx.save_path, "archipelagoOut.sav"), "a").close()


async def check_henry_output(ctx):
    path = os.path.join(ctx.save_path, "archipelagoOut.sav")
    data = ""

    for attempt in range(5):
        try:
            with open(path, "r+", encoding="utf-8") as f:
                data = f.read().strip()

                if data:
                    f.seek(0)
                    f.truncate()

            break

        except PermissionError:
            if attempt == 4:
                raise
            await asyncio.sleep(0.1)

    values = data.split(",") if data else []
    if values:
        await on_locations_checked(ctx, values)

async def on_locations_checked(ctx, locations):
    locIds = henry_name_to_arc_id(locations)
    ctx.locations_checked.update(locIds)

    await ctx.check_locations(locIds)

    if check_if_goal_completed(ctx):
        ctx.finished_game = True
        await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])


    deathlinkReason = get_henry_deathlink_reason(locations,ctx.auth)
    if (deathlinkReason != "None" and ctx.deathlink):
        await ctx.send_death(deathlinkReason)

def add_vanila_progression_items(ctx,henry_item_names):
    final_item_names = henry_item_names

    if (found_BtB_rank(ctx) and ctx.henryslotdata['EtP'] == 3):
        final_item_names.append("Escaping The Prison")

    if (found_EtP_rank(ctx) and ctx.henryslotdata['StD'] == 3):
        final_item_names.append("Stealing The Diamond")

    if (found_StD_rank(ctx) and ctx.henryslotdata['ItA'] == 3):
        final_item_names.append("Infiltraiting The Airship")

    if (found_ItA_rank(ctx) and ctx.henryslotdata['FtC'] == 3):
        final_item_names.append("Fleeing The Complex")

    if (found_FtC_rank(ctx) and ctx.henryslotdata['CtM'] == 3):
        final_item_names.append("Completing The Mission")
    
    return final_item_names

def add_phone_a_friend_items(ctx,henry_item_names):
    final_item_names = henry_item_names
    if ctx.henryslotdata['ItA'] != 0 and ctx.henryslotdata['FtCPhoneAFriendMode'] == 0:
        if (found_Charles_rank(ctx)):
            final_item_names.append("Charles's Phone Number")

        if (found_Reginald_rank(ctx)):
            final_item_names.append("Reginald's Phone Number")
        
    return final_item_names


def add_timeline_items(ctx,henry_item_names):
    final_item_names = henry_item_names
    
    if ctx.henryslotdata['ItA'] != 0 and ctx.henryslotdata['CtMTimelineUnlockMode'] == 0:
        if LOCATION_NAME_TO_ID["ItA: Relentlesss Bounty Hunter"] in get_location_ids(ctx):
            final_item_names.append("Relentless Bounty Hunter Timeline Unlock")

        if LOCATION_NAME_TO_ID["ItA: Government Supported Private Investigator"] in get_location_ids(ctx):
            final_item_names.append("Government Supported Private Investigator Timeline Unlock")

        if LOCATION_NAME_TO_ID["ItA: Rapidly Promoted Executive"] in get_location_ids(ctx):
            final_item_names.append("Rapidly Promoted Executive Timeline Unlock")
        
        if LOCATION_NAME_TO_ID["ItA: Pure Blooded Thief"] in get_location_ids(ctx):
            final_item_names.append("Pure Blooded Thief Timeline Unlock")

    if ctx.henryslotdata['FtC'] != 0 and ctx.henryslotdata['CtMTimelineUnlockMode'] == 0:
        if LOCATION_NAME_TO_ID["FtC: Ghost Inmate"] in get_location_ids(ctx):
            final_item_names.append("Ghost Inmate Timeline Unlock")

        if LOCATION_NAME_TO_ID["FtC: Presumed Dead"] in get_location_ids(ctx):
            final_item_names.append("Presumed Dead Timeline Unlock")

        if LOCATION_NAME_TO_ID["FtC: The Betrayed"] in get_location_ids(ctx):
            final_item_names.append("The Betrayed Timeline Unlock")
        
        if LOCATION_NAME_TO_ID["FtC: Convict Allies"] in get_location_ids(ctx):
            final_item_names.append("Convict Allies Timeline Unlock")

        if LOCATION_NAME_TO_ID["FtC: International Rescue Operative"] in get_location_ids(ctx):
            final_item_names.append("International Rescue Operative Timeline Unlock")
    

    return final_item_names



def update_henry_input(ctx,new_items):
        ctx.all_known_items.extend(new_items)
        henry_item_names = arc_id_to_henry_input_name(ctx.all_known_items)
        henry_item_names = add_vanila_progression_items(ctx,henry_item_names)
        henry_item_names = add_phone_a_friend_items(ctx,henry_item_names)
        henry_item_names = add_timeline_items(ctx,henry_item_names)
        send_items_to_henry(ctx, henry_item_names)


def send_items_to_henry(ctx, henry_item_names):
    henryInPath = os.path.join(ctx.save_path,"archipelagoIn.sav")
    with open(henryInPath, "w", encoding="utf-8") as f:
        f.write(",".join(henry_item_names))

def attempt_find_path(ctx):
    default_path = (Path.home()/ "AppData"/ "Roaming"/ "com.innersloth.henry.HenryFlash"/ "Local Store")
    if (default_path / "main.sav").is_file():
        logger.info(f"Henry Save Data Autodetected at {default_path}")
        ctx.save_path = default_path

