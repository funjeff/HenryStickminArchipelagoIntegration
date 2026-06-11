from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location
from rule_builder.rules import Has, HasAll, Rule

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
    "EtP: Baddass Bust Out" : 27

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

    btbBank = world.get_region("btbIntro")

    btbLocations = get_location_names_with_ids([ "BtB Bank: Shovel Fail", "BtB Bank: Explosives Fail", "BtB Bank: Teleporter Fail", "BtB Bank: Laser Fail", "BtB Bank: Wrecking Ball Fail", "BtB: The Story Begins"])
    btbBank.add_locations(btbLocations,HenryStickminLocation)

    
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

    # Copy of rank locations as event locations to use for goal checking
    the_story_begins_event = HenryStickminLocation(world.player, "The Story Begins Event", None, btbBank)
    btbBank.locations.append(the_story_begins_event)
    world.set_rule(the_story_begins_event,Has("Money Bag Disguise"))

    lawyered_up_event = HenryStickminLocation(world.player, "Lawyered Up Event", None, etpCourtroom)
    etpCourtroom.locations.append(lawyered_up_event)
    world.set_rule(lawyered_up_event,Has("Money Bag Disguise"))

    sneaky_escapist_event = HenryStickminLocation(world.player, "Sneaky Escapist Event", None, etpRooftop)
    etpRooftop.locations.append(sneaky_escapist_event)
    world.set_rule(sneaky_escapist_event,Has("Plungers"))

    badass_bust_out_event = HenryStickminLocation(world.player, "Badass Bust Out Event", None, etpLobby)
    etpLobby.locations.append(badass_bust_out_event)

    #rank event items
    story_begins_event_item = HenryStickminItem("Story Begins Event Item", ItemClassification.progression, None, world.player)
    the_story_begins_event.place_locked_item(story_begins_event_item)

    lawyered_up_event_item = HenryStickminItem("Lawyered Up Event Item", ItemClassification.progression, None, world.player)
    lawyered_up_event.place_locked_item(lawyered_up_event_item)

    sneaky_escapist_event_item = HenryStickminItem("Sneaky Escapist Event Item", ItemClassification.progression, None, world.player)
    sneaky_escapist_event.place_locked_item(sneaky_escapist_event_item)

    badass_bust_event_item = HenryStickminItem("Badass Bust Out Event Item", ItemClassification.progression, None, world.player)
    badass_bust_out_event.place_locked_item(badass_bust_event_item)


    pass
