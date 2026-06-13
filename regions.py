from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

from .henryHelpers import *

from rule_builder.rules import Has, And

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
    
    if use_ItA(world):
        itaBridge = Region("itaBridge", world.player, world.multiworld)
        itaWarehouse = Region("itaWarehouse", world.player, world.multiworld)
        itaQuartersHallway = Region("itaQuartersHallway", world.player, world.multiworld)
        itaBrigDamaged = Region("itaBrigDamaged", world.player, world.multiworld)
        itaShowdownFF = Region("itaShowdownFF", world.player, world.multiworld)
        itaShowdownEB = Region("itaShowdownEB", world.player, world.multiworld)
        itaVentalationShaft = Region("itaVentalationShaft", world.player, world.multiworld)
        itaCargoBayHostage = Region("itaCargoBayHostage", world.player, world.multiworld)

        itaViewingPlatform = Region("itaViewingPlatform", world.player, world.multiworld)
        itaVault = Region("itaVault", world.player, world.multiworld)
        itaOuterWing = Region("itaOuterWing", world.player, world.multiworld)
        itaCenterForChaosContainment = Region("itaCenterForChaosContainment", world.player, world.multiworld)

        itaAirshipTopside = Region("itaAirshipTopside", world.player, world.multiworld)
        itaBoardroom = Region("itaBoardroom", world.player, world.multiworld)
        itaEngineRoomVaultSide = Region("itaEngineRoomVaultSide", world.player, world.multiworld)
        itaEngineVents = Region("itaEngineVents", world.player, world.multiworld)
        itaRecordsLibrary = Region("itaRecordsLibrary", world.player, world.multiworld)
        itaAirDuct = Region("itaAirDuct", world.player, world.multiworld)

        itaCargoBay = Region("itaCargoBay", world.player, world.multiworld)
        itaRegions = [itaBridge,itaWarehouse,itaQuartersHallway,itaBrigDamaged,itaShowdownFF,itaShowdownEB,itaVentalationShaft,itaCargoBayHostage,itaViewingPlatform,itaVault,itaOuterWing,itaCenterForChaosContainment,itaAirshipTopside,itaBoardroom,itaEngineRoomVaultSide,itaEngineVents,itaRecordsLibrary,itaAirDuct,itaCargoBay]
        regions.extend(itaRegions)
    

    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions

def create_region_progression(world,starting_region,regions, rules, pathname):
    prev_region = starting_region
    entrance_num = 0

    for cur_region, rule in zip(regions, rules):
        cur_region_obj = world.get_region(cur_region)
        if rule is not None:
            prev_region.connect(cur_region_obj,f"{pathname} Entrance {entrance_num}",rule)
        else:
            prev_region.connect(cur_region_obj,f"{pathname} Entrance {entrance_num}")
        prev_region = cur_region_obj
        entrance_num += 1

def connect_regions(world: HenryStickminWorld) -> None:
    chapterSelect = world.get_region("chapterSelect")

    if use_BtB(world):
        create_region_progression(world,chapterSelect,["btbIntro"],[Has("Breaking The Bank")],"BtB Progression")

    if use_EtP(world):
        create_region_progression(world,chapterSelect,["etpCell","etpCourtroom"],[get_EtP_unlock_rule(world),Has("Cellphone")],"EtP Lawyered Up Progression")
        
        etpCell = world.get_region("etpCell")
        create_region_progression(world,etpCell,["etpCloset","etpRooftop"],[Has("File"),Has("Chair")],"EtP Sneaky Escapist Progression")
        create_region_progression(world,etpCell,["etpBathroom","etpLobby"],[Has("Drill"),Has("Crowbar")],"EtP Badass Bust Out Progression")
        

    if use_StD(world):
        
        create_region_progression(world,chapterSelect,["stdLookout","stdDiamondExhibitScooter","stdPoliceChaseCar","stdPoliceChaseHeli","stdBridge"],[get_StD_unlock_rule(world),Has("Shield"),Has("Tow Cable"),Has("Rock"),Has("Bubble")],"StD Intruder On A Scooter Progression")
    
        stdLookout = world.get_region("stdLookout")
        create_region_progression(world,stdLookout,["stdRooftop","stdCatwalk","stdDiamondExhibit","stdStorageRoom","stdBackdoor"],[Has("Teleporter"),Has("Penny"),Has("Wire"),Has("Hammer"),Has("Plank")],"StD Unseen Burglar Progression")
        create_region_progression(world,stdLookout,["stdWW2Exhibit","stdRetroExhibit","stdCenterForChaosContainment"],[Has("Pick"),Has("WW2 Plane"),Has("Mushroom")],"StD Just Plain Epic Progression")

    if use_ItA(world):

        create_region_progression(world,chapterSelect,["itaBridge","itaWarehouse","itaQuartersHallway","itaBrigDamaged","itaShowdownFF","itaVentalationShaft","itaCargoBayHostage"],[And(get_ItA_unlock_rule(world), Has("Cannon Ball")),Has("Cannon Ball Chair"),Has("Cannon Ball Eject Button"),Has("Beans"),And(Has("Dirk"),Has("Rocket Launcher")),Has("Chainsaw"),Has("Glider")],"ItA Relentless Bounty Hunter Progression")
        # alternate path defeat right hand man with yo-yo instead of dirk
        itaBrigDamaged = world.get_region("itaBrigDamaged")
        itaShowdownEB = world.get_region("itaShowdownEB")
        itaVentalationShaft = world.get_region("itaVentalationShaft")
        itaBrigDamaged.connect(itaShowdownEB,"Earthbound Entrance", And(Has("Yo-Yo"),Has("Rocket Launcher")))
        itaShowdownEB.connect(itaVentalationShaft,"Multi Bottle Rocket Entrance",Has("Multi bottle rocket"))

        create_region_progression(world,chapterSelect,["itaViewingPlatform","itaVault","itaOuterWing","itaCenterForChaosContainment"],[And(get_ItA_unlock_rule(world),Has("Grapple Gun")),Has("Paperizor"),Has("Shrink 'n Grow"),Has("Armor")],"ItA Pure Blooded Thief Progression")
        create_region_progression(world,chapterSelect,["itaAirshipTopside","itaBoardroom","itaEngineRoomVaultSide","itaEngineVents","itaRecordsLibrary","itaAirDuct"],[And(get_ItA_unlock_rule(world), Has("Earpiece")),Has("Vacuum"),Has("Glue"),Has("Robo Helper"),Has("Bone Melt"),Has("Spider On A Stick")],"ItA Goverment Supported Private Investagator Progression")

        itaCargoBay = world.get_region("itaCargoBay")
        chapterSelect.connect(itaCargoBay,"Sticky Hand Entrance",And(get_ItA_unlock_rule(world),Has("Sticky Hand")))

        
        


