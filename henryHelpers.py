from typing import TYPE_CHECKING
from rule_builder.rules import Has, HasAny

from .options import BtB,EtP, ItA,StD,Required_Ranks

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

def use_ItA(world):
    if world.options.ItA == 1 or world.options.ItA == 2 or world.options.ItA == 3:
        return True
    return False   


def get_BtB_rank_rules():
    return [Has("Story Begins Event Item")]

def get_EtP_rank_rules():
    return[Has("Lawyered Up Event Item"),Has("Sneaky Escapist Event Item"),Has("Badass Bust Out Event Item")]

def get_StD_rank_rules():
    return[Has("Unseen Burglar Event Item"),Has("Intruder On A Scooter Event Item"),Has("Just Plain Epic Event Item")]

def get_ItA_rank_rules():
    return[Has("Relentless Bounty Hunter Event Item"),Has("Government Supported Private Investigator Event Item"),Has("Rapidly Promoted Executive Event Item"),Has("Pure Blooded Thief Event Item")]

def get_BtB_rank_event_item_names():
    return ["Story Begins Event Item"]

def get_EtP_rank_event_item_names():
    return["Lawyered Up Event Item","Sneaky Escapist Event Item","Badass Bust Out Event Item"]

def get_StD_rank_event_item_names():
    return["Unseen Burglar Event Item","Intruder On A Scooter Event Item","Just Plain Epic Event Item"]

def get_ItA_rank_event_item_names():
    return["Relentless Bounty Hunter Event Item","Government Supported Private Investigator Event Item","Rapidly Promoted Executive Event Item","Pure Blooded Thief Event Item"]

def get_EtP_unlock_rule(world):
    if world.options.EtP == EtP.option_yes_vanilla:
        return HasAny(*get_BtB_rank_event_item_names())
    else: 
        return Has("Escaping The Prison")

def get_StD_unlock_rule(world):
    if world.options.StD == StD.option_yes_vanilla:
        return HasAny(*get_EtP_rank_event_item_names())
    else: 
        return Has("Stealing The Diamond")

def get_ItA_unlock_rule(world):
    if world.options.ItA == ItA.option_yes_vanilla:
        return HasAny(*get_StD_rank_event_item_names())
    else: 
        return Has("Infiltraiting The Airship")

