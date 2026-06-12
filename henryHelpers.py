from typing import TYPE_CHECKING
from rule_builder.rules import Has
from .henry_to_arc_names import *

if TYPE_CHECKING:
    from .world import HenryStickminWorld


def use_BtB(world):
    if world.options.BtB == 1 or world.options.BtB == 2:
        return True
    return False


def use_EtP(world):
    if world.options.EtP == 1 or world.options.EtP == 2 or world.options.EtP == 3:
        return True
    return False

def use_StD(world):
    if world.options.StD == 1 or world.options.StD == 2 or world.options.StD == 3:
        return True
    return False

def get_BtB_rank_rules():
    return [Has("Story Begins Event Item")]

def get_EtP_rank_rules():
    return[Has("Lawyered Up Event Item"),Has("Sneaky Escapist Event Item"),Has("Badass Bust Out Event Item")]

def get_StD_rank_rules():
    return[Has("Unseen Burglar Event Item"),Has("Intruder On A Scooter Event Item"),Has("Just Plain Epic Event Item")]

def get_BtB_rank_event_item_names():
    return ["Story Begins Event Item"]

def get_EtP_rank_event_item_names():
    return["Lawyered Up Event Item","Sneaky Escapist Event Item","Badass Bust Out Event Item"]

def get_StD_rank_event_item_names():
    return["Unseen Burglar Event Item","Intruder On A Scooter Event Item","Just Plain Epic Event Item"]


def found_BtB_rank(ctx):
    if henry_name_to_arc_id(["The Story Begins"])[0] in ctx.locations_checked:
        return True
    return False

def found_EtP_rank(ctx):
    if henry_name_to_arc_id(["Lawyered Up"])[0] in ctx.locations_checked:
        return True
    if henry_name_to_arc_id(["Baddass Bust Out"])[0] in ctx.locations_checked:
        return True
    if henry_name_to_arc_id(["Sneaky Escapist"])[0] in ctx.locations_checked:
        return True
    
    return False

def found_StD_rank(ctx):
    if henry_name_to_arc_id(["StD: Intruder On A Scooter"])[0] in ctx.locations_checked:
        return True
    if henry_name_to_arc_id(["Just Plain Epic"])[0] in ctx.locations_checked:
        return True
    if henry_name_to_arc_id(["Unseen Burglar"])[0] in ctx.locations_checked:
        return True
    
    return False