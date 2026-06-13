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
    "ItA Survalliance Room: Elevator Fail" : 134,
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


class HenryStickminLocation(Location):
    game = "Henry Stickmin"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: HenryStickminWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def set_locations_for_region(world,regionName,locations):
    region = world.get_region(regionName)
    locations = get_location_names_with_ids(locations)
    region.add_locations(locations,HenryStickminLocation)

def create_regular_locations(world: HenryStickminWorld) -> None:

    if (use_BtB(world)):
        set_locations_for_region(world,"btbIntro",["BtB Bank: Shovel Fail", "BtB Bank: Explosives Fail", "BtB Bank: Teleporter Fail", "BtB Bank: Laser Fail", "BtB Bank: Wrecking Ball Fail", "BtB: The Story Begins"])

    if (use_EtP(world)):
        set_locations_for_region(world,"etpCell",["EtP Cell: Nrg Drink Fail", "EtP Cell: Teleporter Fail", "EtP Cell: Rocket Launcher Fail"])

        set_locations_for_region(world,"etpCourtroom",["EtP Courtroom: Declared Guilty Fail", "EtP: Lawyered Up"])
        
        set_locations_for_region(world,"etpCloset",["EtP Cell: File Window Fail", "EtP Cell Block: Rupert Kick Fail", "EtP Cell Block: Dave Taser Fail", "EtP Closet: Belt of Grenades Fail", "EtP Closet: Broken Pipe Fail"])
        set_locations_for_region(world,"etpRooftop",["EtP Rooftop: Rope Fail", "EtP Rooftop: Parachute Fail", "EtP Rooftop: JetPack Fail", "EtP: Sneaky Escapist"])
        
        set_locations_for_region(world,"etpBathroom",["EtP Bathroom: Opacitator Fail"])
        set_locations_for_region(world,"etpLobby",["EtP Back Lobby: Pillar Fail", "EtP Back Lobby: Shot Fail", "EtP Lobby Turn: Brawl Fail", "EtP Lobby Turn: Crash Fail: ", "EtP Prison Entrance: Quicktime event Fail", "EtP: Baddass Bust Out"])

    if (use_StD(world)):
        set_locations_for_region(world,"stdLookout",["StD Outer Wall: Liquidificator Fail", "StD Outer Wall: Shrink Ray Fail","StD Outer Wall: Anti-Gravity Cap Fail","StD Outer Wall: Jumble Hoppers Fail","StD Parking Lot: Kick Fail","StD Parking Lot: Jump Fail","StD Parking Lot: Great Start Fail","StD Medieval Hall: Lance Fail","StD Medieval Hall: Flail Fail","StD Medieval Hall: Janitor Fail"])
        
        set_locations_for_region(world,"stdDiamondExhibitScooter",["StD Diamond Exhibit (Scooter): Basket Fail","StD Diamond Exhibit (Scooter): Stand Around Fail"])
        set_locations_for_region(world,"stdPoliceChaseCar",["StD Police Chase Car: Reflexes Fail","StD Police Chase Car: Branch Fail"])
        set_locations_for_region(world,"stdPoliceChaseHeli",["StD Police Chase Helicopter: Headshot Fail","StD Police Chase Helicopter: Sticky Grenade Fail"])
        set_locations_for_region(world,"stdBridge",["StD Bridge: Do Something Fail","StD Bridge: Drive Fail","StD Bridge: Bribe Fail","StD: Intruder On A Scooter"])
        
        set_locations_for_region(world,"stdRooftop",["StD Rooftop: Falcon Punch Fail","StD Rooftop: Tranquilizer Fail","StD Rooftop: Invisibility Pill Fail"])
        set_locations_for_region(world,"stdCatwalk",["StD Catwalk: Drop Fail","StD Catwalk: Wormhole Rifle Fail"])
        set_locations_for_region(world,"stdDiamondExhibit",["StD Diamond Exhibit: Laser Cutter Fail"])
        set_locations_for_region(world,"stdStorageRoom",["StD Storage Room: Cannon Fail","StD Storage Room: Cheese Fail"])
        set_locations_for_region(world,"stdBackdoor",["StD Backdoor: Snap Neck Fail","StD Backdoor: Rifle Fail","StD Backdoor: Jump Fail","StD: Unseen Burglar"])
        
        set_locations_for_region(world,"stdWW2Exhibit",["StD WW2 Exhibit: Dave Conversation Fail","StD WW2 Exhibit: Bomb Fail","StD WW2 Exhibit: Gun Fail"])
        set_locations_for_region(world,"stdRetroExhibit",["StD Diamond Exhibit Entrance: Light Sleeper Fail","StD Retro Exhibit: Alien Fail","StD Retro Exhibit: Goodball Fail","StD Retro Exhibit: Crowbar Fail"])
        set_locations_for_region(world,"stdCenterForChaosContainment",["StD Center For Chaos Containment: Nuclear Bomb Fail","StD Center For Chaos Containment: Divide by Zero Fail","StD Center For Chaos Containment: Shoop da Whoop Fail","StD: Just Plain Epic"])
        
    if (use_ItA(world)):
        set_locations_for_region(world,"itaCargoBay",["ItA Cargo Bay: Zero-Point Energy Fail","ItA Cargo Bay: Ball 'n' Chain Fail"])
        
        set_locations_for_region(world,"itaViewingPlatform",["ItA Viewing Platform: Bomb Fail","ItA Viewing Platform: Joy Buzzer Fail","ItA Viewing Platform: Expanding Foam Fail", "ItA Survalliance Room: Computer Fail","ItA Survalliance Room: Elevator Fail", "ItA Engine Room Records Side: Stretch Chewies Fail","ItA Engine Room Records Side: Magic Pencil Fail","ItA Engine Room Records Side: Teleporter Fail","ItA Brig: Hack Fail","ItA Brig: Wizard Magic Fail","ItA Brig: Retroglove Fail"])
        set_locations_for_region(world,"itaVault",["ItA Vault: Gravity Manipulator Fail","ItA Vault: Clawpack Fail"])
        set_locations_for_region(world,"itaOuterWing",["ItA Outer Wing: Umbrella Fail","ItA Outer Wing: Propane Tank Fail","ItA Outer Wing: Shell Fail"])
        set_locations_for_region(world,"itaCenterForChaosContainment",["ItA Center For Chaos Containment: D.E.B Fail","ItA Center For Chaos Containment: L. Cut mk. II Fail","ItA Center For Chaos Containment: Gaben Fail","ItA: Pure Blooded Thief"])

        set_locations_for_region(world,"itaAirshipTopside",["ItA Airship Topside: Acid Fail","ItA Airship Topside: Knock Fail","ItA Airship Topside: C4 Fail"])
        set_locations_for_region(world,"itaBoardroom",["ItA Boardroom: Disguise Fail","ItA Boardroom: Transdimensionalizer Fail"])
        set_locations_for_region(world,"itaEngineRoomVaultSide",["ItA Engine Room Vault Side: Charles Fail","ItA Engine Room Vault Side: Gravity Bubble Fail","ItA Engine Room Vault Side: Platform Fail"])
        set_locations_for_region(world,"itaEngineVents",["ItA Engine Vents: Gatling Gun Fail","ItA Engine Vents: Mind Control Fail","ItA Engine Vents: Remote Access Fail"])
        set_locations_for_region(world,"itaRecordsLibrary",["ItA Records Library: Ninja Star Fail","ItA Records Library: Duck Propeller Fail","ItA Records Library: Falcon Kick Fail"])
        set_locations_for_region(world,"itaAirDuct",["ItA Air Duct: Don't Need Help Fail","ItA Air Duct: Shut off Power Fail","ItA Cargo Bay Evidence: Banana Bomb Fail","ItA Cargo Bay Evidence: Sleeping Gas Fail","ItA Cargo Bay Evidence: Flashbang Fail","ItA: Government Supported Private Investigator"])

        set_locations_for_region(world,"itaBridge",["ItA Bridge: Laser Fail","ItA Bridge: Thruster Fail"])
        set_locations_for_region(world,"itaWarehouse",["ItA Warehouse: Spikes Fail","ItA Warehouse: COAL-ossal Fail","ItA Warehouse: Boost Fail"])
        set_locations_for_region(world,"itaQuartersHallway",["ItA Quarters Hallway: Warp Fail","ItA Quarters Hallway: Metal Fist Fail","ItA Quarters Hallway: Doors Fail"])
        set_locations_for_region(world,"itaBrigDamaged",["ItA Brig Damaged: Robo Pants Fail","ItA Brig Damaged: Metal Bend Fail"])
        set_locations_for_region(world,"itaShowdownFF",["ItA Dirk Fight:Fight Fail","ItA Dirk Fight: Blitz Fail","ItA Dirk Fight: Magic Fail"])
        set_locations_for_region(world,"itaShowdownEB",["ItA Yo-Yo Fight: Bash Fail","ItA Yo-Yo Fight: PSI Fail","ItA Yo-Yo Fight: Defend Fail"])
        set_locations_for_region(world,"itaVentalationShaft",["ItA Ventalation Shaft: JetBoots Fail","ItA Ventalation Shaft: Beef Up Fail"])
        set_locations_for_region(world,"itaCargoBayHostage",["ItA Cargo Bay Hostage: Parachute Fail","ItA Cargo Bay Hostage: Missile Fail","ItA: Rapidly Promoted Executive","ItA: Relentlesss Bounty Hunter"])


def create_rank_event(world,region,name,rule=None):
    region = world.get_region(region)
    event_location = HenryStickminLocation(world.player, f"{name} Event", None, region)
    region.locations.append(event_location)

    if (rule is not None):
        world.set_rule(event_location,rule)

    event_item = HenryStickminItem(f"{name} Event Item",ItemClassification.progression,None,world.player)
    event_location.place_locked_item(event_item)
    pass


def create_events(world: HenryStickminWorld) -> None:

    # Copy of rank locations as event locations to use for goal checking
    if (use_BtB(world)):
        create_rank_event(world,"btbIntro","Story Begins",Has("Money Bag Disguise"))


    if (use_EtP(world)):
        create_rank_event(world,"etpCourtroom","Lawyered Up",Has("Money Bag Disguise"))
        create_rank_event(world,"etpRooftop","Sneaky Escapist",Has("Plungers"))
        create_rank_event(world,"etpLobby","Badass Bust Out")

    if (use_StD(world)):
        create_rank_event(world,"stdBackdoor","Unseen Burglar",Has("Tunisian Diamond"))
        create_rank_event(world,"stdBridge","Intruder On A Scooter",Has("Tunisian Diamond"))
        create_rank_event(world,"stdCenterForChaosContainment","Just Plain Epic",Has("Giant CCC Robot"))
    
    if (use_ItA(world)):
        create_rank_event(world,"itaCargoBayHostage","Rapidly Promoted Executive",Has("Dummies"))
        create_rank_event(world,"itaCargoBayHostage","Relentless Bounty Hunter",Has("Tank"))
        create_rank_event(world,"itaCenterForChaosContainment","Pure Blooded Thief",Has("Prototype Disk"))
        create_rank_event(world,"itaAirDuct","Government Supported Private Investigator",Has("Force Gun"))
    
