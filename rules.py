from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.field_resolvers import FieldResolver, FromOption
from rule_builder.rules import Has, HasAll, Rule, AtLeast, HasAny
from .options import BtB,EtP, ItA,StD,Required_Ranks

from .henryHelpers import *


if TYPE_CHECKING:
    from .world import HenryStickminWorld



def set_all_rules(world: HenryStickminWorld) -> None:
    # In order for AP to generate an item layout that is actually possible for the player to complete,
    # we need to define rules for our Entrances and Locations.
    # Note: Regions do not have rules, the Entrances connecting them do!
    # We'll do entrances first, then locations, and then finally we set our victory condition.

    set_all_location_rules(world)
    set_completion_condition(world)


    # Conditions can also depend on event items. TODO use this for CtM

def set_location_rule(world,location,rule):
    loc = world.get_location(location)
    world.set_rule(loc,rule)


def set_all_location_rules(world: HenryStickminWorld) -> None:
    if (use_BtB(world)):
        set_location_rule(world,"BtB Bank: Shovel Fail",Has("Shovel"))
        set_location_rule(world,"BtB Bank: Explosives Fail",Has("Explosives"))
        set_location_rule(world,"BtB Bank: Teleporter Fail",Has("Teleporter"))
        set_location_rule(world,"BtB Bank: Laser Fail",Has("Laser"))
        set_location_rule(world,"BtB Bank: Wrecking Ball Fail",Has("Wrecking Ball"))
        set_location_rule(world,"BtB: The Story Begins",Has("Money Bag Disguise"))
                
    if (use_EtP(world)):
        set_location_rule(world,"EtP Cell: Nrg Drink Fail",Has("Nrg Drink"))
        set_location_rule(world,"EtP Cell: Teleporter Fail",Has("Teleporter"))
        set_location_rule(world,"EtP Cell: Rocket Launcher Fail",Has("Rocket Launcher"))
        set_location_rule(world,"EtP Closet: Belt of Grenades Fail",Has("Belt of Grenades"))
        set_location_rule(world,"EtP Closet: Broken Pipe Fail",Has("Chair"))
        set_location_rule(world,"EtP Rooftop: Rope Fail",Has("Rope Launcher"))
        set_location_rule(world,"EtP Rooftop: Parachute Fail",Has("Parachute"))
        set_location_rule(world,"EtP Rooftop: JetPack Fail",Has("JetPack"))
        set_location_rule(world,"EtP: Sneaky Escapist",Has("Plungers"))

        set_location_rule(world,"EtP Courtroom: Declared Guilty Fail",Has("Attorney's Badge") | Has("Floor Plans of Bank") | Has("Doctor's Analysis") | Has("Security Footage") | Has("Teleporter"))
        set_location_rule(world,"EtP: Lawyered Up",Has("Money Bag Disguise"))
        
        set_location_rule(world,"EtP Bathroom: Opacitator Fail",Has("Opacitator"))

    if (use_StD(world)):
        set_location_rule(world,"StD Outer Wall: Liquidificator Fail",Has("Liquidificator"))
        set_location_rule(world,"StD Outer Wall: Shrink Ray Fail",Has("Shrink Ray"))
        set_location_rule(world,"StD Outer Wall: Anti-Gravity Cap Fail",Has("Anti-Gravity Cap"))
        set_location_rule(world,"StD Outer Wall: Jumble Hoppers Fail",Has("Jumble Hoppers"))
        set_location_rule(world,"StD Rooftop: Falcon Punch Fail",Has("Falcon Punch"))
        set_location_rule(world,"StD Rooftop: Tranquilizer Fail",Has("Tranquilizer"))
        set_location_rule(world,"StD Rooftop: Invisibility Pill Fail",Has("Invisibility Pill"))
        set_location_rule(world,"StD Catwalk: Wormhole Rifle Fail",Has("Wormhole Rifle"))
        set_location_rule(world,"StD Diamond Exhibit: Laser Cutter Fail",Has("Laser Cutter"))
        set_location_rule(world,"StD Storage Room: Cannon Fail",Has("Cannon"))
        set_location_rule(world,"StD Storage Room: Cheese Fail",Has("Cheese"))
        set_location_rule(world,"StD Backdoor: Rifle Fail",Has("Rifle"))
        set_location_rule(world,"StD: Unseen Burglar",Has("Tunisian Diamond"))

        set_location_rule(world,"StD WW2 Exhibit: Bomb Fail",Has("WW2 Bomb"))
        set_location_rule(world,"StD WW2 Exhibit: Gun Fail",Has("WW2 Gun"))
        set_location_rule(world,"StD Retro Exhibit: Alien Fail",Has("Metroid"))
        set_location_rule(world,"StD Retro Exhibit: Goodball Fail",Has("Goodball"))
        set_location_rule(world,"StD Retro Exhibit: Crowbar Fail",Has("Crowbar"))
        set_location_rule(world,"StD Center For Chaos Containment: Nuclear Bomb Fail",Has("Nuclear Bomb"))
        set_location_rule(world,"StD Center For Chaos Containment: Divide by Zero Fail",Has("Division By Zero"))
        set_location_rule(world,"StD: Just Plain Epic",Has("Giant CCC Robot"))

        set_location_rule(world,"StD Medieval Hall: Lance Fail",Has("Lance"))
        set_location_rule(world,"StD Medieval Hall: Flail Fail",Has("Flail"))
        set_location_rule(world,"StD Diamond Exhibit (Scooter): Basket Fail",Has("Basket"))
        set_location_rule(world,"StD Police Chase Car: Branch Fail",Has("Branch"))
        set_location_rule(world,"StD Police Chase Helicopter: Sticky Grenade Fail",Has("Sticky Grenade"))
        set_location_rule(world,"StD: Intruder On A Scooter",Has("Tunisian Diamond"))
    
    if (use_ItA(world)):

        set_location_rule(world,"ItA Cargo Bay: Zero-Point Energy Fail",Has("Zero-Point Energy"))
        set_location_rule(world,"ItA Cargo Bay: Ball 'n' Chain Fail",Has("Ball 'n Chain"))

        set_location_rule(world,"ItA Viewing Platform: Bomb Fail",Has("Bomb"))
        set_location_rule(world,"ItA Viewing Platform: Joy Buzzer Fail",Has("Joy Buzzer"))
        set_location_rule(world,"ItA Viewing Platform: Expanding Foam Fail",Has("Expanding Foam"))
        set_location_rule(world,"ItA Engine Room Records Side: Stretch Chewies Fail",Has("Stretch Chewies"))
        set_location_rule(world,"ItA Engine Room Records Side: Magic Pencil Fail",Has("Magic Pencil"))
        set_location_rule(world,"ItA Engine Room Records Side: Teleporter Fail",Has("Teleporter"))
        set_location_rule(world,"ItA Brig: Wizard Magic Fail",Has("Wizard Magic"))
        set_location_rule(world,"ItA Brig: Retroglove Fail",Has("Retroglove"))
        set_location_rule(world,"ItA Vault: Gravity Manipulator Fail",Has("Gravity Manipulator"))
        set_location_rule(world,"ItA Vault: Clawpack Fail",Has("Clawpack"))
        set_location_rule(world,"ItA Outer Wing: Umbrella Fail",Has("Umbrella"))
        set_location_rule(world,"ItA Outer Wing: Propane Tank Fail",Has("Propane Tank"))
        set_location_rule(world,"ItA Outer Wing: Shell Fail",Has("Shell"))
        set_location_rule(world,"ItA Center For Chaos Containment: D.E.B Fail",Has("D.E.B Disk"))
        set_location_rule(world,"ItA Center For Chaos Containment: L. Cut mk. II Fail",Has("L. Cut mk. II Disk"))
        set_location_rule(world,"ItA Center For Chaos Containment: Gaben Fail",Has("Scratched Disk"))
        set_location_rule(world,"ItA: Pure Blooded Thief",Has("Prototype Disk"))

        set_location_rule(world,"ItA Airship Topside: Acid Fail",Has("Acid"))
        set_location_rule(world,"ItA Airship Topside: C4 Fail",Has("C4"))
        set_location_rule(world,"ItA Boardroom: Disguise Fail",Has("Toppat Disguise"))
        set_location_rule(world,"ItA Boardroom: Transdimensionalizer Fail",Has("Transdimensionalizer"))
        set_location_rule(world,"ItA Engine Room Vault Side: Gravity Bubble Fail",Has("Gravity Bubble"))
        set_location_rule(world,"ItA Engine Room Vault Side: Platform Fail",Has("Platform"))
        set_location_rule(world,"ItA Engine Vents: Gatling Gun Fail",Has("Gatling Gun"))
        set_location_rule(world,"ItA Engine Vents: Mind Control Fail",Has("Mind Control"))
        set_location_rule(world,"ItA Engine Vents: Remote Access Fail",Has("Remote Access"))
        set_location_rule(world,"ItA Records Library: Ninja Star Fail",Has("Ninja Star"))
        set_location_rule(world,"ItA Records Library: Falcon Kick Fail",Has("Falcon Kick"))
        set_location_rule(world,"ItA Cargo Bay Evidence: Banana Bomb Fail",Has("Banana Bomb"))
        set_location_rule(world,"ItA Cargo Bay Evidence: Sleeping Gas Fail",Has("Sleeping Gas"))
        set_location_rule(world,"ItA Cargo Bay Evidence: Flashbang Fail",Has("Flashbang"))
        set_location_rule(world,"ItA: Government Supported Private Investigator",Has("Force Gun"))

        set_location_rule(world,"ItA Bridge: Laser Fail",Has("Cannon Ball Laser"))
        set_location_rule(world,"ItA Bridge: Thruster Fail",Has("Cannon Ball Thruster"))
        set_location_rule(world,"ItA Warehouse: Spikes Fail",Has("Cannon Ball Spikes"))
        set_location_rule(world,"ItA Warehouse: Boost Fail",Has("Cannon Ball Boost"))
        set_location_rule(world,"ItA Quarters Hallway: Warp Fail",Has("Warp"))
        set_location_rule(world,"ItA Quarters Hallway: Metal Fist Fail",Has("Metal Fist"))
        set_location_rule(world,"ItA Brig Damaged: Robo Pants Fail",Has("Robo Pants"))        
        set_location_rule(world,"ItA Brig Damaged: Metal Bend Fail",Has("Metalbending"))
        set_location_rule(world,"ItA Yo-Yo Fight: PSI Fail",Has("PSI Flash"))
        set_location_rule(world,"ItA Dirk Fight: Magic Fail",Has("Fire Magic"))
        set_location_rule(world,"ItA Ventalation Shaft: JetBoots Fail",Has("JetBoots"))
        set_location_rule(world,"ItA Ventalation Shaft: Beef Up Fail",Has("Beef Up"))
        set_location_rule(world,"ItA Cargo Bay Hostage: Parachute Fail",Has("Parachute"))
        set_location_rule(world,"ItA Cargo Bay Hostage: Missile Fail",Has("Missile"))
        set_location_rule(world,"ItA: Rapidly Promoted Executive",Has("Dummies"))
        set_location_rule(world,"ItA: Relentlesss Bounty Hunter",Has("Tank"))


def set_completion_condition(world: HenryStickminWorld) -> None:
    if world.options.Goal == 0:
        obtainable_ranks = []
        if use_BtB(world):
            obtainable_ranks.extend(get_BtB_rank_rules())
        if use_EtP(world):
            obtainable_ranks.extend(get_EtP_rank_rules())
        if use_StD(world):
            obtainable_ranks.extend(get_StD_rank_rules())
        if use_ItA(world):
            obtainable_ranks.extend(get_ItA_rank_rules())
        
        world.set_completion_rule(AtLeast(FromOption(Required_Ranks),*obtainable_ranks) )
    
    if world.options.Goal == 2:
        btbCheck = HasAny(*get_BtB_rank_event_item_names(),options=[OptionFilter(BtB,BtB.option_no,operator="ne")],filtered_resolution=True)
        etpCheck = HasAny(*get_EtP_rank_event_item_names(),options=[OptionFilter(EtP,EtP.option_no,operator="ne")],filtered_resolution=True)
        stdCheck = HasAny(*get_StD_rank_event_item_names(),options=[OptionFilter(StD,StD.option_no,operator="ne")],filtered_resolution=True)
        itaCheck = HasAny(*get_ItA_rank_event_item_names(),options=[OptionFilter(ItA,ItA.option_no,operator="ne")],filtered_resolution=True)
        world.set_completion_rule(btbCheck & etpCheck & stdCheck & itaCheck)



# One final comment about rules:
# If your world exclusively uses Rule Builder rules (like APQuest), it's worth trying CachedRuleBuilderWorld.
# CachedRuleBuilderWorld is a subclass of World that has a bunch of caching magic to make rules faster.
# Just have your world class subclass CachedRuleBuilderWorld instead of World:
#   class APQuestWorld(CachedRuleBuilderWorld): ...
# This may speed up your world, or it may make it slower.
# The exact factors are complex and not well understood, but there is no harm in trying it.
# Generate a few seeds and see if there is a noticeable difference!
# If you're wondering, author has checked: APQuest is too simple to see any benefits, so we'll stick with "World".
