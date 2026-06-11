from typing import TYPE_CHECKING
from rule_builder.rules import Has

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

def get_BtB_rank_rules():
    return [Has("Story Begins Event Item")]

def get_EtP_rank_rules():
    return[Has("Lawyered Up Event Item"),Has("Sneaky Escapist Event Item"),Has("Badass Bust Out Event Item")]

def get_BtB_rank_event_item_names():
    return ["Story Begins Event Item"]

def get_EtP_rank_event_item_names():
    return["Lawyered Up Event Item","Sneaky Escapist Event Item","Badass Bust Out Event Item"]
