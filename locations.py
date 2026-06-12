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
    "StD: Intruder On A Scooter" : 70

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


    pass
