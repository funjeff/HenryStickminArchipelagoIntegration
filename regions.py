from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

from .henryHelpers import *

if TYPE_CHECKING:
    from .world import HenryStickminWorld


def create_and_connect_regions(world: HenryStickminWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: HenryStickminWorld) -> None:
    regions = []

    chapterSelect = Region("chapterSelect",world.player,world.multiworld)
    regions.append(chapterSelect)

    # Creating a region is as simple as calling the constructor of the Region class.
    if use_BtB(world):
        btbBank = Region("btbIntro", world.player, world.multiworld)
        regions.append(btbBank)
    
    if use_EtP(world):
        etpCell = Region("etpCell", world.player, world.multiworld)
        etpCourtroom = Region("etpCourtroom", world.player, world.multiworld)
        etpCloset = Region("etpCloset", world.player, world.multiworld)
        etpRooftop = Region("etpRooftop", world.player, world.multiworld)
        etpBathroom = Region("etpBathroom", world.player, world.multiworld)
        etpLobby = Region("etpLobby", world.player, world.multiworld)
        etpRegions = [etpCell, etpCourtroom, etpCloset,etpRooftop,etpBathroom,etpLobby]
        regions.extend(etpRegions)
        

    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: HenryStickminWorld) -> None:
    chapterSelect = world.get_region("chapterSelect")

    if use_BtB(world):
        btbBank = world.get_region("btbIntro")
        chapterSelect.connect(btbBank, "btb_entrance")

    if use_EtP(world):
        etpCell = world.get_region("etpCell")
        etpCourtroom = world.get_region("etpCourtroom")
        etpCloset = world.get_region("etpCloset")
        etpRooftop = world.get_region("etpRooftop")
        etpBathroom = world.get_region("etpBathroom")
        etpLobby = world.get_region("etpLobby")

        chapterSelect.connect(etpCell, "etp_entrance")

        etpCell.connect(etpCourtroom, "Cellphone")
        etpCell.connect(etpCloset, "File")
        etpCloset.connect(etpRooftop, "Chair")

        etpCell.connect(etpBathroom, "Drill")
        etpBathroom.connect(etpLobby, "Crowbar")
