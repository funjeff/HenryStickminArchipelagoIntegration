from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.field_resolvers import FromOption
from rule_builder.rules import Has, HasAll, Rule, AtLeast, HasAny
from .options import BtB,EtP,Required_Ranks

from .henryHelpers import *


if TYPE_CHECKING:
    from .world import HenryStickminWorld



def set_all_rules(world: HenryStickminWorld) -> None:
    # In order for AP to generate an item layout that is actually possible for the player to complete,
    # we need to define rules for our Entrances and Locations.
    # Note: Regions do not have rules, the Entrances connecting them do!
    # We'll do entrances first, then locations, and then finally we set our victory condition.

    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: HenryStickminWorld) -> None:
    if use_BtB(world):
        btbLevelSelect = world.get_entrance("btb_entrance")
        world.set_rule(btbLevelSelect,Has("Breaking The Bank"))
    
    
    if use_EtP(world):
        cellphone = world.get_entrance("Cellphone")
        file = world.get_entrance("File")
        chair = world.get_entrance("Chair")
        drill = world.get_entrance("Drill")
        crowbar = world.get_entrance("Crowbar")

        etpLevelSelect = world.get_entrance("etp_entrance")

        if world.options.EtP == EtP.option_yes_vanilla:
            world.set_rule(etpLevelSelect,HasAny(*get_BtB_rank_event_item_names()))
        else: 
            world.set_rule(etpLevelSelect,Has("Escaping The Prison"))

        world.set_rule(cellphone,Has("Cellphone"))
        world.set_rule(file,Has("File"))
        world.set_rule(chair,Has("Chair"))
        world.set_rule(drill,Has("Drill"))
        world.set_rule(crowbar,Has("Crowbar"))




    # Conditions can also depend on event items. TODO use this for CtM


def set_all_location_rules(world: HenryStickminWorld) -> None:
    if (use_BtB(world)):
        BtBShovelFail = world.get_location("BtB Bank: Shovel Fail")
        world.set_rule(BtBShovelFail,Has("Shovel"))
        
        BtBExplosivesFail = world.get_location("BtB Bank: Explosives Fail")
        world.set_rule(BtBExplosivesFail,Has("Explosives"))
        
        BtBTeleporterFail = world.get_location("BtB Bank: Teleporter Fail")
        world.set_rule(BtBTeleporterFail,Has("Teleporter"))
        
        BtBLaserFail = world.get_location("BtB Bank: Laser Fail")
        world.set_rule(BtBLaserFail,Has("Laser"))
        
        BtBWreckingBallFail = world.get_location("BtB Bank: Wrecking Ball Fail")
        world.set_rule(BtBWreckingBallFail,Has("Wrecking Ball"))
        
        BtBStoryBegins = world.get_location("BtB: The Story Begins")
        world.set_rule(BtBStoryBegins,Has("Money Bag Disguise"))
        
    if (use_EtP(world)):
        EtPNRGFail = world.get_location("EtP Cell: Nrg Drink Fail")
        world.set_rule(EtPNRGFail,Has("Nrg Drink"))

        EtPTeleporterFail = world.get_location("EtP Cell: Teleporter Fail")
        world.set_rule(EtPTeleporterFail,Has("Teleporter"))

        EtPRocketLauncherFail = world.get_location("EtP Cell: Rocket Launcher Fail")
        world.set_rule(EtPRocketLauncherFail,Has("Rocket Launcher"))

        EtPBeltOfGrenadesFail = world.get_location("EtP Closet: Belt of Grenades Fail")
        world.set_rule(EtPBeltOfGrenadesFail,Has("Belt of Grenades"))

        EtPBrokenPipeFail = world.get_location("EtP Closet: Broken Pipe Fail")
        world.set_rule(EtPBrokenPipeFail,Has("Chair"))

        EtPRopeFail = world.get_location("EtP Rooftop: Rope Fail")
        world.set_rule(EtPRopeFail,Has("Rope Launcher"))

        EtPParachuteFail = world.get_location("EtP Rooftop: Parachute Fail")
        world.set_rule(EtPParachuteFail,Has("Parachute"))

        EtPJetpackFail = world.get_location("EtP Rooftop: JetPack Fail")
        world.set_rule(EtPJetpackFail,Has("JetPack"))

        EtPSneakyEscapist = world.get_location("EtP: Sneaky Escapist")
        world.set_rule(EtPSneakyEscapist,Has("Plungers"))

        EtPGuiltyFail = world.get_location("EtP Courtroom: Declared Guilty Fail")
        world.set_rule(EtPGuiltyFail,Has("Attorney's Badge") | Has("Floor Plans of Bank") | Has("Doctor's Analysis") | Has("Security Footage") | Has("Teleporter"))

        EtPLawyeredUp = world.get_location("EtP: Lawyered Up")
        world.set_rule(EtPLawyeredUp,Has("Money Bag Disguise"))

        EtPOpacitatorFail = world.get_location("EtP Bathroom: Opacitator Fail")
        world.set_rule(EtPOpacitatorFail,Has("Opacitator"))
        


def set_completion_condition(world: HenryStickminWorld) -> None:
    if world.options.Goal == 0:
        obtainable_ranks = []
        if use_BtB(world):
            obtainable_ranks.extend(get_BtB_rank_rules())
        if use_EtP(world):
            obtainable_ranks.extend(get_EtP_rank_rules())
        
        world.set_completion_rule(AtLeast(FromOption(Required_Ranks),*obtainable_ranks) )
    
    if world.options.Goal == 2:
        btbCheck = HasAny(*get_BtB_rank_event_item_names(),options=[OptionFilter(BtB,BtB.option_no,operator="ne")],filtered_resolution=True)
        etpCheck = HasAny(*get_EtP_rank_event_item_names(),options=[OptionFilter(EtP,EtP.option_no,operator="ne")],filtered_resolution=True)
        world.set_completion_rule(btbCheck & etpCheck)



# One final comment about rules:
# If your world exclusively uses Rule Builder rules (like APQuest), it's worth trying CachedRuleBuilderWorld.
# CachedRuleBuilderWorld is a subclass of World that has a bunch of caching magic to make rules faster.
# Just have your world class subclass CachedRuleBuilderWorld instead of World:
#   class APQuestWorld(CachedRuleBuilderWorld): ...
# This may speed up your world, or it may make it slower.
# The exact factors are complex and not well understood, but there is no harm in trying it.
# Generate a few seeds and see if there is a noticeable difference!
# If you're wondering, author has checked: APQuest is too simple to see any benefits, so we'll stick with "World".
