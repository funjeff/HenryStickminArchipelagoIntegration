HENRY_NAME_TO_LOC_NAME = {
    "shovel":"BtB Bank: Shovel Fail",
    "explosives":"BtB Bank: Explosives Fail",
    "teleporter":"BtB Bank: Teleporter Fail",
    "laser":"BtB Bank: Laser Fail",
    "wreckingball":"BtB Bank: Wrecking Ball Fail",
    "The Story Begins":"BtB: The Story Begins",
    "etp_nrg":"EtP Cell: Nrg Drink Fail",
    "etp_teleporter":"EtP Cell: Teleporter Fail",
    "etp_rocket":"EtP Cell: Rocket Launcher Fail",
    "etp_fileWindow":"EtP Cell: File Window Fail",
    "etp_timed1":"EtP Cell Block: Rupert Kick Fail",
    "etp_timed2":"EtP Cell Block: Dave Taser Fail",
    "etp_grenade":"EtP Closet: Belt of Grenades Fail",
    "etp_ventLeft":"EtP Closet: Broken Pipe Fail",
    "etp_rope":"EtP Rooftop: Rope Fail",
    "etp_parachute":"EtP Rooftop: Parachute Fail",
    "etp_jetpack":"EtP Rooftop: JetPack Fail",
    "Sneaky Escapist":"EtP: Sneaky Escapist",
    "etp_cellphone":"EtP Courtroom: Declared Guilty Fail",
    "Lawyered Up":"EtP: Lawyered Up",
    "etp_opacitator":"EtP Bathroom: Opacitator Fail",
    "etp_chase1Up":"EtP Back Lobby: Pillar Fail",
    "etp_chase1Time":"EtP Back Lobby: Shot Fail",
    "etp_chase2Down":"EtP Lobby Turn: Brawl Fail",
    "etp_chase2Time":"EtP Lobby Turn: Crash Fail: ",
    "etp_timedFinal":"EtP Prison Entrance: Quicktime event Fail",
    "Baddass Bust Out":"EtP: Baddass Bust Out"
}

# HENRY_NAME_TO_DEATHLINK_REASON = {
#     "shovel":"Henry Dug Strate Down",

# }

from .locations import LOCATION_NAME_TO_ID

from .items import ID_TO_ITEM_NAME




def henry_name_to_arc_id(henryName):
    arcIds = []
    for name in henryName:
        arcName = HENRY_NAME_TO_LOC_NAME[name]
        arcIds.append(LOCATION_NAME_TO_ID[arcName])
    return arcIds

def arc_id_to_henry_input_name(id):
    henryInputNames = []
    for idnum in id:
        inputName = ID_TO_ITEM_NAME[idnum.item]
        henryInputNames.append(inputName)
    return henryInputNames

def get_henry_deathlink_reason(henryName):
    return "None"


def get_num_BtB_ranks_achived(ctx):
    num_btb_ranks = 0
    if LOCATION_NAME_TO_ID["BtB: The Story Begins"] in ctx.locations_checked:
        num_btb_ranks = num_btb_ranks + 1
    return num_btb_ranks

def get_num_EtP_ranks_achived(ctx):
    num_etp_ranks = 0
    if LOCATION_NAME_TO_ID["EtP: Lawyered Up"] in ctx.locations_checked:
        num_etp_ranks = num_etp_ranks + 1

    if LOCATION_NAME_TO_ID["EtP Rooftop: Rope Fail"] in ctx.locations_checked:
        num_etp_ranks = num_etp_ranks + 1

    if LOCATION_NAME_TO_ID["EtP: Baddass Bust Out"] in ctx.locations_checked:
        num_etp_ranks = num_etp_ranks + 1

    return num_etp_ranks

def check_if_goal_completed(ctx):
    if ctx.henryslotdata['Goal'] == 0:
        total_ranks = 0
        if ctx.henryslotdata['BtB'] != 0:
            total_ranks = total_ranks + get_num_BtB_ranks_achived(ctx)
        if ctx.henryslotdata['EtP'] != 0:
            total_ranks = total_ranks + get_num_EtP_ranks_achived(ctx)
        if total_ranks >= ctx.henryslotdata['Required_Ranks']:
            return True
    elif ctx.henryslotdata['Goal'] == 2:
        if ctx.henryslotdata['BtB'] != 0 and get_num_BtB_ranks_achived(ctx) < 1:
            return False
        if ctx.henryslotdata['EtP'] != 0 and get_num_EtP_ranks_achived(ctx) < 1:
            return False
        return True
    return False
        
        