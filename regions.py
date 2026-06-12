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
    
    if use_StD(world):
        stdLookout = Region("stdLookout", world.player, world.multiworld)
        stdDiamondExhibitScooter = Region("stdDiamondExhibitScooter", world.player, world.multiworld)
        stdPoliceChaseCar = Region("stdPoliceChaseCar", world.player, world.multiworld)
        stdPoliceChaseHeli = Region("stdPoliceChaseHeli", world.player, world.multiworld)
        stdBridge = Region("stdBridge", world.player, world.multiworld)

        stdRooftop = Region("stdRooftop", world.player, world.multiworld)
        stdCatwalk = Region("stdCatwalk", world.player, world.multiworld)
        stdDiamondExhibit = Region("stdDiamondExhibit", world.player, world.multiworld)
        stdStorageRoom = Region("stdStorageRoom", world.player, world.multiworld)
        stdBackdoor = Region("stdBackdoor", world.player, world.multiworld)

        stdWW2Exhibit = Region("stdWW2Exhibit", world.player, world.multiworld)
        stdRetroExhibit = Region("stdRetroExhibit", world.player, world.multiworld)
        stdCenterForChaosContainment = Region("stdCenterForChaosContainment", world.player, world.multiworld)
        stdRegions = [stdLookout, stdDiamondExhibitScooter, stdPoliceChaseCar,stdPoliceChaseHeli,stdBridge,stdRooftop,stdCatwalk,stdDiamondExhibit,stdStorageRoom,stdBackdoor,stdWW2Exhibit,stdRetroExhibit,stdCenterForChaosContainment]
        regions.extend(stdRegions)

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

    if use_StD(world):
        stdLookout = world.get_region("stdLookout")
        stdDiamondExhibitScooter = world.get_region("stdDiamondExhibitScooter")
        stdPoliceChaseCar = world.get_region("stdPoliceChaseCar")
        stdPoliceChaseHeli = world.get_region("stdPoliceChaseHeli")
        stdBridge = world.get_region("stdBridge")

        stdRooftop = world.get_region("stdRooftop")
        stdCatwalk = world.get_region("stdCatwalk")
        stdDiamondExhibit = world.get_region("stdDiamondExhibit")
        stdStorageRoom = world.get_region("stdStorageRoom")
        stdBackdoor = world.get_region("stdBackdoor")

        stdWW2Exhibit = world.get_region("stdWW2Exhibit")
        stdRetroExhibit = world.get_region("stdRetroExhibit")
        stdCenterForChaosContainment = world.get_region("stdCenterForChaosContainment")

        chapterSelect.connect(stdLookout, "std_entrance")

        stdLookout.connect(stdDiamondExhibitScooter, "Shield")
        stdDiamondExhibitScooter.connect(stdPoliceChaseCar,"Tow Cable")
        stdPoliceChaseCar.connect(stdPoliceChaseHeli,"Rock")
        stdPoliceChaseHeli.connect(stdBridge,"Bubble")

        stdLookout.connect(stdRooftop, "Teleporter")
        stdRooftop.connect(stdCatwalk, "Penny")
        stdCatwalk.connect(stdDiamondExhibit, "Wire")
        stdDiamondExhibit.connect(stdStorageRoom, "Hammer")
        stdStorageRoom.connect(stdBackdoor, "Plank")

        stdLookout.connect(stdWW2Exhibit, "Pick")
        stdWW2Exhibit.connect(stdRetroExhibit,"Plane")
        stdRetroExhibit.connect(stdCenterForChaosContainment,"Mushroom")
        
        


