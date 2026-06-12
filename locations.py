from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location
from rule_builder.rules import Has, HasAll, Rule

from .henryHelpers import *
from .items import HenryStickminItem

if TYPE_CHECKING:
    from . import HenryStickminWorld

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
LOCATION_NAME_TO_ID = {
    "BtB Bank: Shovel Fail": 1,
    "BtB Bank: Explosives Fail": 2,
    "BtB Bank: Teleporter Fail": 3,
    "BtB Bank: Laser Fail": 4,
    "BtB Bank: Wrecking Ball Fail": 5,
    "BtB: The Story Begins": 6,
    "EtP Cell: Nrg Drink Fail": 7,
    "EtP Cell: Teleporter Fail": 8,
    "EtP Cell: Rocket Launcher Fail": 9,
    "EtP Cell: File Window Fail": 10,
    "EtP Cell Block: Rupert Kick Fail": 11,
    "EtP Cell Block: Dave Taser Fail": 12,
    "EtP Closet: Belt of Grenades Fail": 13,
    "EtP Closet: Broken Pipe Fail": 14,
    "EtP Rooftop: Rope Fail": 15,
    "EtP Rooftop: Parachute Fail": 16,
    "EtP Rooftop: JetPack Fail": 17,
    "EtP: Sneaky Escapist": 18,
    "EtP Courtroom: Declared Guilty Fail": 19,
    "EtP: Lawyered Up": 20,
    "EtP Bathroom: Opacitator Fail" : 21,
    "EtP Back Lobby: Pillar Fail" : 22,
    "EtP Back Lobby: Shot Fail" : 23,
    "EtP Lobby Turn: Brawl Fail" : 24,
    "EtP Lobby Turn: Crash Fail: " : 25,
    "EtP Prison Entrance: Quicktime event Fail" : 26,
    "EtP: Baddass Bust Out" : 27,
    "StD Outer Wall: Liquidificator Fail" : 28,
    "StD Outer Wall: Shrink Ray Fail" : 29,
    "StD Outer Wall: Anti-Gravity Cap Fail" : 30,
    "StD Outer Wall: Jumble Hoppers Fail" : 31,
    "StD Rooftop: Falcon Punch Fail" : 32,
    "StD Rooftop: Tranquilizer Fail" : 33,
    "StD Rooftop: Invisibility Pill Fail" : 34,
    "StD Catwalk: Drop Fail" : 35,
    "StD Catwalk: Wormhole Rifle Fail" : 36,
    "StD Diamond Exhibit: Laser Cutter Fail" : 37,
    "StD Storage Room: Cannon Fail" : 38,
    "StD Storage Room: Cheese Fail" : 39,
    "StD Backdoor: Snap Neck Fail" : 40,
    "StD Backdoor: Rifle Fail" : 41,
    "StD Backdoor: Jump Fail" : 42,
    "StD: Unseen Burglar" : 52,
    "StD WW2 Exhibit: Dave Conversation Fail" : 43,
    "StD WW2 Exhibit: Bomb Fail" : 44,
    "StD WW2 Exhibit: Gun Fail" : 45,
    "StD Diamond Exhibit Entrance: Light Sleeper Fail" : 46,
    "StD Retro Exhibit: Alien Fail" : 47,
    "StD Retro Exhibit: Goodball Fail" : 48,
    "StD Retro Exhibit: Crowbar Fail" : 49,
    "StD Center For Chaos Containment: Nuclear Bomb Fail" : 50,
    "StD Center For Chaos Containment: Divide by Zero Fail" : 51,
    "StD Center For Chaos Containment: Shoop da Whoop Fail" : 53,
    "StD: Just Plain Epic" : 54,
    "StD Parking Lot: Kick Fail" : 55,
    "StD Parking Lot: Jump Fail" : 56,
    "StD Parking Lot: Great Start Fail" : 57,
    "StD Medieval Hall: Lance Fail" : 58,
    "StD Medieval Hall: Flail Fail" : 59,
    "StD Medieval Hall: Janitor Fail" : 60,
    "StD Diamond Exhibit (Scooter): Basket Fail" : 61,
    "StD Diamond Exhibit (Scooter): Stand Around Fail" : 62,
    "StD Police Chase Car: Reflexes Fail" : 63,
    "StD Police Chase Car: Branch Fail" : 64,
    "StD Police Chase Helicopter: Headshot Fail" : 65,
    "StD Police Chase Helicopter: Sticky Grenade Fail" : 66,
    "StD Bridge: Do Something Fail" : 67,
    "StD Bridge: Drive Fail" : 68,
    "StD Bridge: Bribe Fail" : 69,
    "StD: Intruder On A Scooter" : 70,
    "ItA Cargo Bay: Zero-Point Energy Fail" : 71,
    "ItA Cargo Bay: Ball 'n' Chain Fail" : 72,
    "ItA Viewing Platform: Bomb Fail" : 73,
    "ItA Viewing Platform: Joy Buzzer Fail" : 74,
    "ItA Viewing Platform: Expanding Foam Fail" : 75,
    "ItA Survalliance Room: Computer Fail" : 76,
    "ItA Survalliance Room: Elevator Fail" : 76,
    "ItA Engine Room Records Side: Stretch Chewies Fail" : 77,
    "ItA Engine Room Records Side: Magic Pencil Fail" : 78,
    "ItA Engine Room Records Side: Teleporter Fail" : 79,
    "ItA Brig: Hack Fail" : 80,
    "ItA Brig: Wizard Magic Fail" : 81,
    "ItA Brig: Retroglove Fail" : 82,
    "ItA Vault: Gravity Manipulator Fail" : 83,
    "ItA Vault: Clawpack Fail" : 84,
    "ItA Outer Wing: Umbrella Fail" : 85,
    "ItA Outer Wing: Propane Tank Fail" : 86,
    "ItA Outer Wing: Shell Fail" : 87,
    "ItA Center For Chaos Containment: D.E.B Fail" : 88,
    "ItA Center For Chaos Containment: L. Cut mk. II Fail" : 89,
    "ItA Center For Chaos Containment: Gaben Fail" : 90,
    "ItA: Pure Blooded Thief":91,
    "ItA Airship Topside: Acid Fail":92,
    "ItA Airship Topside: Knock Fail":93,
    "ItA Airship Topside: C4 Fail":94,
    "ItA Boardroom: Disguise Fail":95,
    "ItA Boardroom: Transdimensionalizer Fail":96,
    "ItA Engine Room Vault Side: Charles Fail":97,
    "ItA Engine Room Vault Side: Gravity Bubble Fail":98,
    "ItA Engine Room Vault Side: Platform Fail":99,
    "ItA Engine Vents: Gatling Gun Fail":100,
    "ItA Engine Vents: Mind Control Fail":101,
    "ItA Engine Vents: Remote Access Fail":102,
    "ItA Records Library: Ninja Star Fail":103,
    "ItA Records Library: Duck Propeller Fail":104,
    "ItA Records Library: Falcon Kick Fail":105,
    "ItA Air Duct: Don't Need Help Fail":106,
    "ItA Air Duct: Shut off Power Fail":107,
    "ItA Cargo Bay Evidence: Banana Bomb Fail":108,
    "ItA Cargo Bay Evidence: Sleeping Gas Fail":109,
    "ItA Cargo Bay Evidence: Flashbang Fail":110,
    "ItA: Government Supported Private Investigator":111,
    "ItA Bridge: Laser Fail":112,
    "ItA Bridge: Thruster Fail":113,
    "ItA Warehouse: Spikes Fail":114,
    "ItA Warehouse: COAL-ossal Fail":115,
    "ItA Warehouse: Boost Fail":116,
    "ItA Quarters Hallway: Warp Fail":117,
    "ItA Quarters Hallway: Metal Fist Fail":118,
    "ItA Quarters Hallway: Doors Fail":119,
    "ItA Brig Damaged: Robo Pants Fail":120,
    "ItA Brig Damaged: Metal Bend Fail":121,
    "ItA Yo-Yo Fight: Bash Fail":122,
    "ItA Yo-Yo Fight: PSI Fail":123,
    "ItA Yo-Yo Fight: Defend Fail":124,
    "ItA Dirk Fight:Fight Fail":125,
    "ItA Dirk Fight: Blitz Fail":126,
    "ItA Dirk Fight: Magic Fail":127,
    "ItA Ventalation Shaft: JetBoots Fail":128,
    "ItA Ventalation Shaft: Beef Up Fail":129,
    "ItA Cargo Bay Hostage: Parachute Fail":130,
    "ItA Cargo Bay Hostage: Missile Fail":131,
    "ItA: Rapidly Promoted Executive":132,
    "ItA: Relentlesss Bounty Hunter":133
}


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class HenryStickminLocation(Location):
    game = "Henry Stickmin"


# Let's make one more helper method before we begin actually creating locations.
# Later on in the code, we'll want specific subsections of LOCATION_NAME_TO_ID.
# To reduce the chance of copy-paste errors writing something like {"Chest": LOCATION_NAME_TO_ID["Chest"]},
# let's make a helper method that takes a list of location names and returns them as a dict with their IDs.
# Note: There is a minor typing quirk here. Some functions want location addresses to be an "int | None",
# so while our function here only ever returns dict[str, int], we annotate it as dict[str, int | None].
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: HenryStickminWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: HenryStickminWorld) -> None:

    if (use_BtB(world)):
        btbBank = world.get_region("btbIntro")

        btbLocations = get_location_names_with_ids([ "BtB Bank: Shovel Fail", "BtB Bank: Explosives Fail", "BtB Bank: Teleporter Fail", "BtB Bank: Laser Fail", "BtB Bank: Wrecking Ball Fail", "BtB: The Story Begins"])
        btbBank.add_locations(btbLocations,HenryStickminLocation)

    if (use_EtP(world)):    
        etpCell = world.get_region("etpCell")
        etpCellLocations = get_location_names_with_ids(["EtP Cell: Nrg Drink Fail", "EtP Cell: Teleporter Fail", "EtP Cell: Rocket Launcher Fail"])
        etpCell.add_locations(etpCellLocations,HenryStickminLocation)
        
        etpCourtroom = world.get_region("etpCourtroom")
        etpCourtroomLocations = get_location_names_with_ids(["EtP Courtroom: Declared Guilty Fail", "EtP: Lawyered Up"])
        etpCourtroom.add_locations(etpCourtroomLocations,HenryStickminLocation)

        etpCloset = world.get_region("etpCloset")
        etpClosetLocations = get_location_names_with_ids(["EtP Cell: File Window Fail", "EtP Cell Block: Rupert Kick Fail", "EtP Cell Block: Dave Taser Fail", "EtP Closet: Belt of Grenades Fail", "EtP Closet: Broken Pipe Fail"])
        etpCloset.add_locations(etpClosetLocations,HenryStickminLocation)

        etpRooftop = world.get_region("etpRooftop")
        etpRooftopLocations = get_location_names_with_ids(["EtP Rooftop: Rope Fail", "EtP Rooftop: Parachute Fail", "EtP Rooftop: JetPack Fail", "EtP: Sneaky Escapist"])
        etpRooftop.add_locations(etpRooftopLocations,HenryStickminLocation)

        etpBathroom = world.get_region("etpBathroom")
        etpBathroomLocations = get_location_names_with_ids(["EtP Bathroom: Opacitator Fail"])
        etpBathroom.add_locations(etpBathroomLocations,HenryStickminLocation)

        etpLobby = world.get_region("etpLobby")
        etpLobbyLocations = get_location_names_with_ids(["EtP Back Lobby: Pillar Fail", "EtP Back Lobby: Shot Fail", "EtP Lobby Turn: Brawl Fail", "EtP Lobby Turn: Crash Fail: ", "EtP Prison Entrance: Quicktime event Fail", "EtP: Baddass Bust Out"])
        etpLobby.add_locations(etpLobbyLocations)
    
    if (use_StD(world)):
        stdLookout = world.get_region("stdLookout")
        stdLookoutLocations = get_location_names_with_ids(["StD Outer Wall: Liquidificator Fail", "StD Outer Wall: Shrink Ray Fail","StD Outer Wall: Anti-Gravity Cap Fail","StD Outer Wall: Jumble Hoppers Fail","StD Parking Lot: Kick Fail","StD Parking Lot: Jump Fail","StD Parking Lot: Great Start Fail","StD Medieval Hall: Lance Fail","StD Medieval Hall: Flail Fail","StD Medieval Hall: Janitor Fail"])
        stdLookout.add_locations(stdLookoutLocations)

        stdDiamondExhibitScooter = world.get_region("stdDiamondExhibitScooter")
        stdDiamondExhibitScooterLocations = get_location_names_with_ids(["StD Diamond Exhibit (Scooter): Basket Fail","StD Diamond Exhibit (Scooter): Stand Around Fail"])
        stdDiamondExhibitScooter.add_locations(stdDiamondExhibitScooterLocations)

        stdPoliceChaseCar = world.get_region("stdPoliceChaseCar")
        stdPoliceChaseCarLocations = get_location_names_with_ids(["StD Police Chase Car: Reflexes Fail","StD Police Chase Car: Branch Fail"])
        stdPoliceChaseCar.add_locations(stdPoliceChaseCarLocations)
        
        stdPoliceChaseHeli = world.get_region("stdPoliceChaseHeli")
        stdPoliceChaseHeliLocations = get_location_names_with_ids(["StD Police Chase Helicopter: Headshot Fail","StD Police Chase Helicopter: Sticky Grenade Fail"])
        stdPoliceChaseHeli.add_locations(stdPoliceChaseHeliLocations)
        
        stdBridge = world.get_region("stdBridge")
        stdBridgeLocations = get_location_names_with_ids(["StD Bridge: Do Something Fail","StD Bridge: Drive Fail","StD Bridge: Bribe Fail","StD: Intruder On A Scooter"])
        stdBridge.add_locations(stdBridgeLocations)


        stdRooftop = world.get_region("stdRooftop")
        stdRooftopLocations = get_location_names_with_ids(["StD Rooftop: Falcon Punch Fail","StD Rooftop: Tranquilizer Fail","StD Rooftop: Invisibility Pill Fail"])
        stdRooftop.add_locations(stdRooftopLocations)

        stdCatwalk = world.get_region("stdCatwalk")
        stdCatwalkLocations = get_location_names_with_ids(["StD Catwalk: Drop Fail","StD Catwalk: Wormhole Rifle Fail"])
        stdCatwalk.add_locations(stdCatwalkLocations)

        stdDiamondExhibit = world.get_region("stdDiamondExhibit")
        stdDiamondExhibitLocations = get_location_names_with_ids(["StD Diamond Exhibit: Laser Cutter Fail"])
        stdDiamondExhibit.add_locations(stdDiamondExhibitLocations)

        stdStorageRoom = world.get_region("stdStorageRoom")
        stdStorageRoomLocations = get_location_names_with_ids(["StD Storage Room: Cannon Fail","StD Storage Room: Cheese Fail"])
        stdStorageRoom.add_locations(stdStorageRoomLocations)

        stdBackdoor = world.get_region("stdBackdoor")
        stdBackdoorLocations = get_location_names_with_ids(["StD Backdoor: Snap Neck Fail","StD Backdoor: Rifle Fail","StD Backdoor: Jump Fail","StD: Unseen Burglar"])
        stdBackdoor.add_locations(stdBackdoorLocations)

        stdWW2Exhibit = world.get_region("stdWW2Exhibit")
        stdWW2ExhibitLocations = get_location_names_with_ids(["StD WW2 Exhibit: Dave Conversation Fail","StD WW2 Exhibit: Bomb Fail","StD WW2 Exhibit: Gun Fail"])
        stdWW2Exhibit.add_locations(stdWW2ExhibitLocations)

        stdRetroExhibit = world.get_region("stdRetroExhibit")
        stdRetroExhibitLocations = get_location_names_with_ids(["StD Diamond Exhibit Entrance: Light Sleeper Fail","StD Retro Exhibit: Alien Fail","StD Retro Exhibit: Goodball Fail","StD Retro Exhibit: Crowbar Fail"])
        stdRetroExhibit.add_locations(stdRetroExhibitLocations)

        stdCenterForChaosContainment = world.get_region("stdCenterForChaosContainment")
        stdCenterForChaosContainmentLocations = get_location_names_with_ids(["StD Center For Chaos Containment: Nuclear Bomb Fail","StD Center For Chaos Containment: Divide by Zero Fail","StD Center For Chaos Containment: Shoop da Whoop Fail","StD: Just Plain Epic"])
        stdCenterForChaosContainment.add_locations(stdCenterForChaosContainmentLocations)

    if (use_ItA(world)):
        itaCargoBay = world.get_region("itaCargoBay")
        itaCargoBayLocations = get_location_names_with_ids(["ItA Cargo Bay: Zero-Point Energy Fail","ItA Cargo Bay: Ball 'n' Chain Fail"])
        itaCargoBay.add_locations(itaCargoBayLocations)

        itaViewingPlatform = world.get_region("itaViewingPlatform")
        itaViewingPlatformLocations = get_location_names_with_ids(["ItA Viewing Platform: Bomb Fail","ItA Viewing Platform: Joy Buzzer Fail","ItA Viewing Platform: Expanding Foam Fail, ItA Survalliance Room: Computer Fail","ItA Survalliance Room: Elevator Fail, ItA Engine Room Records Side: Stretch Chewies Fail","ItA Engine Room Records Side: Magic Pencil Fail","ItA Engine Room Records Side: Teleporter Fail","ItA Brig: Hack Fail","ItA Brig: Wizard Magic Fail","ItA Brig: Retroglove Fail"])
        itaViewingPlatform.add_locations(itaViewingPlatformLocations)

        itaVault = world.get_region("itaVault")
        itaVaultLocations = get_location_names_with_ids(["ItA Vault: Gravity Manipulator Fail","ItA Vault: Clawpack Fail"])
        itaVault.add_locations(itaVaultLocations)

        itaOuterWing = world.get_region("itaOuterWing")
        itaOuterWingLocations = get_location_names_with_ids(["ItA Outer Wing: Umbrella Fail","ItA Outer Wing: Propane Tank Fail","ItA Outer Wing: Shell Fail"])
        itaOuterWing.add_locations(itaOuterWingLocations)

        itaCenterForChaosContainment = world.get_region("itaCenterForChaosContainment")
        itaCenterForChaosContainmentLocations = get_location_names_with_ids(["ItA Center For Chaos Containment: D.E.B Fail","ItA Center For Chaos Containment: L. Cut mk. II Fail","ItA Center For Chaos Containment: Gaben Fail","ItA: Pure Blooded Thief"])
        itaCenterForChaosContainment.add_locations(itaCenterForChaosContainmentLocations)

        itaAirshipTopside = world.get_region("itaAirshipTopside")
        itaAirshipTopsideLocations = get_location_names_with_ids(["ItA Airship Topside: Acid Fail","ItA Airship Topside: Knock Fail","ItA Airship Topside: C4 Fail","ItA Boardroom: Disguise Fail","ItA Boardroom: Transdimensionalizer Fail"])
        itaAirshipTopside.add_locations(itaAirshipTopsideLocations)

        itaEngineRoomVaultSide = world.get_region("itaEngineRoomVaultSide")
        itaEngineRoomVaultSideLocations = get_location_names_with_ids(["ItA Engine Room Vault Side: Charles Fail","ItA Engine Room Vault Side: Gravity Bubble Fail","ItA Engine Room Vault Side: Platform Fail"])
        itaEngineRoomVaultSide.add_locations(itaEngineRoomVaultSideLocations)

        itaEngineVents = world.get_region("itaEngineVents")
        itaEngineVentsLocations = get_location_names_with_ids(["ItA Engine Vents: Gatling Gun Fail","ItA Engine Vents: Mind Control Fail","ItA Engine Vents: Remote Access Fail"])
        itaEngineVents.add_locations(itaEngineVentsLocations)

        itaRecordsLibrary = world.get_region("itaRecordsLibrary")
        itaRecordsLibraryLocations = get_location_names_with_ids(["ItA Records Library: Ninja Star Fail","ItA Records Library: Duck Propeller Fail","ItA Records Library: Falcon Kick Fail"])
        itaRecordsLibrary.add_locations(itaRecordsLibraryLocations)

        itaAirDuct = world.get_region("itaAirDuct")
        itaAirDuctLocations = get_location_names_with_ids(["ItA Air Duct: Don't Need Help Fail","ItA Air Duct: Shut off Power Fail","ItA Cargo Bay Evidence: Banana Bomb Fail","ItA Cargo Bay Evidence: Sleeping Gas Fail","ItA Cargo Bay Evidence: Flashbang Fail","ItA: Government Supported Private Investigator"])
        itaAirDuct.add_locations(itaAirDuctLocations)

        itaBridge = world.get_region("itaBridge")
        itaBridgeLocations = get_location_names_with_ids(["ItA Bridge: Laser Fail","ItA Bridge: Thruster Fail"])
        itaBridge.add_locations(itaBridgeLocations)

        itaWarehouse = world.get_region("itaWarehouse")
        itaWarehouseLocations = get_location_names_with_ids(["ItA Warehouse: Spikes Fail","ItA Warehouse: COAL-ossal Fail","ItA Warehouse: Boost Fail"])
        itaWarehouse.add_locations(itaWarehouseLocations)

        itaQuartersHallway = world.get_region("itaQuartersHallway")
        itaQuartersHallwayLocations = get_location_names_with_ids(["ItA Quarters Hallway: Warp Fail","ItA Quarters Hallway: Metal Fist Fail","ItA Quarters Hallway: Doors Fail"])
        itaQuartersHallway.add_locations(itaQuartersHallwayLocations)
                                                                             
        itaBrigDamaged = world.get_region("itaBrigDamaged")
        itaBrigDamagedLocations = get_location_names_with_ids(["ItA Brig Damaged: Robo Pants Fail","ItA Brig Damaged: Metal Bend Fail"])
        itaBrigDamaged.add_locations(itaBrigDamagedLocations)

        itaShowdownFF = world.get_region("itaShowdownFF")
        itaShowdownFFLocations = get_location_names_with_ids(["ItA Dirk Fight:Fight Fail","ItA Dirk Fight: Blitz Fail","ItA Dirk Fight: Magic Fail"])
        itaShowdownFF.add_locations(itaShowdownFFLocations)

        itaShowdownEB = world.get_region("itaShowdownEB")
        itaShowdownEBLocations = get_location_names_with_ids(["ItA Yo-Yo Fight: Bash Fail","ItA Yo-Yo Fight: PSI Fail","ItA Yo-Yo Fight: Defend Fail"])
        itaShowdownEB.add_locations(itaShowdownEBLocations)

        itaVentalationShaft = world.get_region("itaVentalationShaft")
        itaVentalationShaftLocations = get_location_names_with_ids(["ItA Ventalation Shaft: JetBoots Fail","ItA Ventalation Shaft: Beef Up Fail"])
        itaVentalationShaft.add_locations(itaVentalationShaftLocations)

        itaCargoBayHostage = world.get_region("itaCargoBayHostage")
        itaCargoBayHostageLocations = get_location_names_with_ids(["ItA Cargo Bay Hostage: Parachute Fail","ItA Cargo Bay Hostage: Missile Fail","ItA: Rapidly Promoted Executive","ItA: Relentlesss Bounty Hunter"])
        itaCargoBayHostage.add_locations(itaCargoBayHostageLocations)


def create_events(world: HenryStickminWorld) -> None:
    # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    # In our case, the player must press a button in the top left room to open the final boss door.
    # AP has something for this purpose: "Event locations" and "Event items".
    # An event location is no different than a regular location, except it has the address "None".
    # It is treated during generation like any other location, but then it is discarded.
    # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
    # top_left_room = world.get_region("Top Left Room")
    # final_boss_room = world.get_region("Final Boss Room")

    btbBank = world.get_region("btbIntro")
    etpCourtroom = world.get_region("etpCourtroom")
    etpRooftop = world.get_region("etpRooftop")
    etpLobby = world.get_region("etpLobby")
    stdBackdoor = world.get_region("stdBackdoor")
    stdCenterForChaosContainment = world.get_region("stdCenterForChaosContainment")
    stdBridge = world.get_region("stdBridge")
    itaCargoBayHostage = world.get_region("itaCargoBayHostage")
    itaCenterForChaosContainment = world.get_region("itaCenterForChaosContainment")
    itaAirDuct = world.get_region("itaAirDuct")

    # Copy of rank locations as event locations to use for goal checking
    if (use_BtB(world)):
        the_story_begins_event = HenryStickminLocation(world.player, "The Story Begins Event", None, btbBank)
        btbBank.locations.append(the_story_begins_event)
        world.set_rule(the_story_begins_event,Has("Money Bag Disguise"))

        story_begins_event_item = HenryStickminItem("Story Begins Event Item", ItemClassification.progression, None, world.player)
        the_story_begins_event.place_locked_item(story_begins_event_item)


    if (use_EtP(world)):
        lawyered_up_event = HenryStickminLocation(world.player, "Lawyered Up Event", None, etpCourtroom)
        etpCourtroom.locations.append(lawyered_up_event)
        world.set_rule(lawyered_up_event,Has("Money Bag Disguise"))

        sneaky_escapist_event = HenryStickminLocation(world.player, "Sneaky Escapist Event", None, etpRooftop)
        etpRooftop.locations.append(sneaky_escapist_event)
        world.set_rule(sneaky_escapist_event,Has("Plungers"))

        badass_bust_out_event = HenryStickminLocation(world.player, "Badass Bust Out Event", None, etpLobby)
        etpLobby.locations.append(badass_bust_out_event)

        lawyered_up_event_item = HenryStickminItem("Lawyered Up Event Item", ItemClassification.progression, None, world.player)
        lawyered_up_event.place_locked_item(lawyered_up_event_item)

        sneaky_escapist_event_item = HenryStickminItem("Sneaky Escapist Event Item", ItemClassification.progression, None, world.player)
        sneaky_escapist_event.place_locked_item(sneaky_escapist_event_item)

        badass_bust_event_item = HenryStickminItem("Badass Bust Out Event Item", ItemClassification.progression, None, world.player)
        badass_bust_out_event.place_locked_item(badass_bust_event_item)
    
    if (use_StD(world)):
        unseen_burglar_event = HenryStickminLocation(world.player, "Unseen Burglar Event", None, stdBackdoor)
        stdBackdoor.locations.append(unseen_burglar_event)
        world.set_rule(unseen_burglar_event,Has("Tunisian Diamond"))

        intruder_on_a_scooter_event = HenryStickminLocation(world.player, "Intruder On A Scooter Event", None, stdBridge)
        stdBridge.locations.append(intruder_on_a_scooter_event)
        world.set_rule(intruder_on_a_scooter_event,Has("Tunisian Diamond"))

        just_plain_epic_event = HenryStickminLocation(world.player, "Just Plain Epic Event", None, stdCenterForChaosContainment)
        stdCenterForChaosContainment.locations.append(just_plain_epic_event)
        world.set_rule(just_plain_epic_event,Has("Giant CCC Robot"))

        unseen_burglar_event_item = HenryStickminItem("Unseen Burglar Event Item", ItemClassification.progression, None, world.player)
        unseen_burglar_event.place_locked_item(unseen_burglar_event_item)

        intruder_on_a_scooter_event_item = HenryStickminItem("Intruder On A Scooter Event Item", ItemClassification.progression, None, world.player)
        intruder_on_a_scooter_event.place_locked_item(intruder_on_a_scooter_event_item)

        just_plain_epic_event_item = HenryStickminItem("Just Plain Epic Event Item", ItemClassification.progression, None, world.player)
        just_plain_epic_event.place_locked_item(just_plain_epic_event_item)
    
    if (use_ItA(world)):
        pure_blooded_thief_event = HenryStickminLocation(world.player, "Pure Blooded Thief Event", None, itaCenterForChaosContainment)
        itaCenterForChaosContainment.locations.append(pure_blooded_thief_event)
        world.set_rule(pure_blooded_thief_event,Has("Prototype Disk"))

        rapidly_promoted_executive_event = HenryStickminLocation(world.player, "Rapidly Promoted Executive Event", None, itaCargoBayHostage)
        itaCargoBayHostage.locations.append(rapidly_promoted_executive_event)
        world.set_rule(rapidly_promoted_executive_event,Has("Dummies"))

        relentless_bounty_hunter_event = HenryStickminLocation(world.player, "Relentless Bounty Hunter Event", None, itaCargoBayHostage)
        itaCargoBayHostage.locations.append(relentless_bounty_hunter_event)
        world.set_rule(relentless_bounty_hunter_event,Has("Tank"))

        government_supported_private_investigator_event = HenryStickminLocation(world.player, "Government Supported Private Investigator Event", None, itaAirDuct)
        itaAirDuct.locations.append(government_supported_private_investigator_event)
        world.set_rule(government_supported_private_investigator_event,Has("Force Gun"))

        pure_blooded_thief_event_item = HenryStickminItem("Pure Blooded Thief Event Item", ItemClassification.progression, None, world.player)
        pure_blooded_thief_event.place_locked_item(pure_blooded_thief_event_item)

        rapidly_promoted_executive_event_item = HenryStickminItem("Rapidly Promoted Executive Event Item", ItemClassification.progression, None, world.player)
        rapidly_promoted_executive_event.place_locked_item(rapidly_promoted_executive_event_item)

        relentless_bounty_hunter_event_item = HenryStickminItem("Relentless Bounty Hunter Event Item", ItemClassification.progression, None, world.player)
        relentless_bounty_hunter_event.place_locked_item(relentless_bounty_hunter_event_item)

        government_supported_private_investigator_event_item = HenryStickminItem("Government Supported Private Investigator Event Item", ItemClassification.progression, None, world.player)
        government_supported_private_investigator_event.place_locked_item(government_supported_private_investigator_event_item)
    
    