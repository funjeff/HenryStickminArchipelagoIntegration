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
        self.ctx.deathlink = not self.ctx.deathlink

class HenryContext(CommonContext):
    game = "The Henry Stickmin Collection"
    save_path = ""
    items_sent_to_henry = []
    command_processor = HenryCommandProcessor
    items_handling = 0b111
    henryslotdata = None
    deathlink = False

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            self.henryslotdata = args['slot_data']
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
    henryOutPath = os.path.join(ctx.save_path,"archipelagoOut.sav")
    with open(henryOutPath, "r+", encoding="utf-8") as f:
        data = f.read().strip()
        f.seek(0)
        f.truncate()

    values = data.split(",") if data else []
    if (values):
        await on_locations_checked(ctx,values)

async def on_locations_checked(ctx, locations):
    locIds = henry_name_to_arc_id(locations)

    checked = set(ctx.locations_checked)
    ctx.locations_checked.update(
        loc_id for loc_id in locIds
        if loc_id not in checked
    )

    if check_if_goal_completed(ctx):
        ctx.finished_game = True
        await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])

    await ctx.check_locations(locIds)
    deathlinkReason = get_henry_deathlink_reason(locations,ctx.auth)
    if (deathlinkReason != "None" and ctx.deathlink):
        await ctx.send_death(deathlinkReason)

def add_vanila_progression_items(ctx,henry_item_names):
    final_item_names = henry_item_names

    if (found_BtB_rank() and ctx.henryslotdata['EtP'] == 3):
        final_item_names.append("Escaping The Prison")

    if (found_EtP_rank() and ctx.henryslotdata['StD'] == 3):
        final_item_names.append("Stealing The Diamond")
    
    return final_item_names


def update_henry_input(ctx,new_items):
        ctx.items_sent_to_henry.extend(new_items)
        henry_item_names = arc_id_to_henry_input_name(ctx.items_sent_to_henry)
        henry_item_names = add_vanila_progression_items(ctx,henry_item_names)
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

