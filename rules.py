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
    
    if use_StD(world):
        shield = world.get_entrance("Shield")
        tow_cable = world.get_entrance("Tow Cable")
        rock = world.get_entrance("Rock")
        bubble = world.get_entrance("Bubble")
        teleporter = world.get_entrance("Teleporter")
        penny = world.get_entrance("Penny")
        wire = world.get_entrance("Wire")
        hammer = world.get_entrance("Hammer")
        plank = world.get_entrance("Plank")
        pick = world.get_entrance("Pick")
        plane = world.get_entrance("Plane")
        mushroom = world.get_entrance("Mushroom")

        stdLevelSelect = world.get_entrance("std_entrance")
        if world.options.StD == StD.option_yes_vanilla:
            world.set_rule(stdLevelSelect,HasAny(*get_EtP_rank_event_item_names()))
        else: 
            world.set_rule(stdLevelSelect,Has("Stealing The Diamond"))
        world.set_rule(shield,Has("Shield"))
        tow_cable.set_rule(Has("Tow Cable"))
        rock.set_rule(Has("Rock"))
        bubble.set_rule(Has("Bubble"))
        teleporter.set_rule(Has("Teleporter"))
        penny.set_rule(Has("Penny"))
        wire.set_rule(Has("Wire"))
        hammer.set_rule(Has("Hammer"))
        plank.set_rule(Has("Plank"))
        pick.set_rule(Has("Pick"))
        plane.set_rule(Has("WW2 Plane"))
        mushroom.set_rule(Has("Mushroom"))
    
    if use_ItA(world):
        cannon_ball = world.get_entrance("Cannon Ball")
        cannon_ball_chair = world.get_entrance("Cannon Ball Chair")
        cannon_ball_eject_button = world.get_entrance("Cannon Ball Eject Button")
        beans = world.get_entrance("Beans")
        dirk_and_rocket_launcher = world.get_entrance("DirkandRocketLauncher")
        yo_yo_and_rocket_launcher = world.get_entrance("Yo-YoandRocketLauncher")
        chainsaw = world.get_entrance("Chainsaw")
        multi_bottle_rocket = world.get_entrance("Multi bottle rocket")
        glider = world.get_entrance("Glider")

        grapple_gun = world.get_entrance("Grapple Gun")
        paperizor = world.get_entrance("Paperizor")
        armor = world.get_entrance("Armor")

        earpiece = world.get_entrance("Earpiece")
        glue = world.get_entrance("Glue")
        robo_helper = world.get_entrance("Robo Helper")
        bone_melt = world.get_entrance("Bone Melt")
        spider_on_a_stick = world.get_entrance("Spider On A Stick")

        sticky_hand = world.get_entrance("Sticky Hand")


        itaLevelSelect = world.get_entrance("ita_entrance")
        if world.options.ItA == ItA.option_yes_vanilla:
            world.set_rule(itaLevelSelect,HasAny(*get_StD_rank_event_item_names()))
        else: 
            world.set_rule(itaLevelSelect,Has("Infiltrating the Airship"))
        
        cannon_ball.set_rule(Has("Cannon Ball"))
        cannon_ball_chair.set_rule(Has("Cannon Ball Chair"))
        cannon_ball_eject_button.set_rule(Has("Cannon Ball Eject Button"))
        beans.set_rule(Has("Beans"))
        dirk_and_rocket_launcher.set_rule(Has("Dirk") & Has("Rocket Launcher"))
        yo_yo_and_rocket_launcher.set_rule(Has("Yo-Yo") & Has("Rocket Launcher"))
        chainsaw.set_rule(Has("Chainsaw"))
        multi_bottle_rocket.set_rule(Has("Multi bottle rocket"))
        glider.set_rule(Has("Glider"))

        grapple_gun.set_rule(Has("Grapple Gun"))
        paperizor.set_rule(Has("Paperizor"))
        armor.set_rule(Has("Armor"))

        earpiece.set_rule(Has("Earpiece"))
        glue.set_rule(Has("Glue"))
        robo_helper.set_rule(Has("Robo Helper"))
        bone_melt.set_rule(Has("Bone Melt"))
        spider_on_a_stick.set_rule(Has("Spider On A Stick"))

        sticky_hand.set_rule(Has("Sticky Hand"))



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

    if (use_StD(world)):
        StDLiquidificatorFail = world.get_location("StD Outer Wall: Liquidificator Fail")
        world.set_rule(StDLiquidificatorFail,Has("Liquidificator"))   

        StDShrinkRayFail = world.get_location("StD Outer Wall: Shrink Ray Fail")
        world.set_rule(StDShrinkRayFail,Has("Shrink Ray"))   
        
        StDAntiGravityCapFail = world.get_location("StD Outer Wall: Anti-Gravity Cap Fail")
        world.set_rule(StDAntiGravityCapFail,Has("StDAntiGravityCapFail"))   
        
        StDJumbleHoppersFail = world.get_location("StD Outer Wall: Jumble Hoppers Fail")
        world.set_rule(StDJumbleHoppersFail,Has("Jumble Hoppers"))   

        StDFalconPunchFail = world.get_location("StD Rooftop: Falcon Punch Fail")
        world.set_rule(StDFalconPunchFail,Has("Falcon Punch"))   

        StDTranquilizerFail = world.get_location("StD Rooftop: Tranquilizer Fail")
        world.set_rule(StDTranquilizerFail,Has("Tranquilizer"))   

        StDInvisibilityPillFail = world.get_location("StD Rooftop: Invisibility Pill Fail")
        world.set_rule(StDInvisibilityPillFail,Has("Invisibility Pill")) 

        StDWormholeRifleFail = world.get_location("StD Catwalk: Wormhole Rifle Fail")
        world.set_rule(StDWormholeRifleFail,Has("Wormhole Rifle"))   

        StDLaserCutterFail = world.get_location("StD Diamond Exhibit: Laser Cutter Fail")
        world.set_rule(StDLaserCutterFail,Has("Laser Cutter"))   

        StDCannonFail = world.get_location("StD Storage Room: Cannon Fail")
        world.set_rule(StDCannonFail,Has("Cannon"))   

        StDCheeseFail = world.get_location("StD Storage Room: Cheese Fail")
        world.set_rule(StDCheeseFail,Has("Cheese"))

        StDRifleFail = world.get_location("StD Backdoor: Rifle Fail")
        world.set_rule(StDRifleFail,Has("Rifle"))

        StDUnseenBurglar = world.get_location("StD: Unseen Burglar")
        world.set_rule(StDUnseenBurglar,Has("Tunisian Diamond"))

        StDBombFail = world.get_location("StD WW2 Exhibit: Bomb Fail")
        world.set_rule(StDBombFail,Has("WW2 Bomb"))

        StDGunFail = world.get_location("StD WW2 Exhibit: Gun Fail")
        world.set_rule(StDGunFail,Has("WW2 Gun"))

        StDAlienFail = world.get_location("StD Retro Exhibit: Alien Fail")
        world.set_rule(StDAlienFail,Has("Metroid"))

        StDGoodballFail = world.get_location("StD Retro Exhibit: Goodball Fail")
        world.set_rule(StDGoodballFail,Has("Goodball"))

        StDCrowbarFail = world.get_location("StD Retro Exhibit: Crowbar Fail")
        world.set_rule(StDCrowbarFail,Has("Crowbar"))
    
        StDNukeFail = world.get_location("StD Center For Chaos Containment: Nuclear Bomb Fail")
        world.set_rule(StDNukeFail,Has("Nuclear Bomb"))

        StDDividebyZeroFail = world.get_location("StD Center For Chaos Containment: Divide by Zero Fail")
        world.set_rule(StDDividebyZeroFail,Has("Division By Zero"))

        StDShoopDaWhoopFail = world.get_location("StD Center For Chaos Containment: Shoop da Whoop Fail")
        world.set_rule(StDShoopDaWhoopFail,Has("Shoop da Whoop"))

        StDJustPlainEpic = world.get_location("StD: Just Plain Epic")
        world.set_rule(StDJustPlainEpic,Has("Giant CCC Robot"))

        StDLanceFail = world.get_location("StD Medieval Hall: Lance Fail")
        world.set_rule(StDLanceFail,Has("Lance"))

        StDFlailFail = world.get_location("StD Medieval Hall: Flail Fail")
        world.set_rule(StDFlailFail,Has("Flail"))

        StDBasketFail = world.get_location("StD Diamond Exhibit (Scooter): Basket Fail")
        world.set_rule(StDBasketFail,Has("Basket"))

        StDBranchFail = world.get_location("StD Police Chase Car: Branch Fail")
        world.set_rule(StDBranchFail,Has("Branch"))

        StDStickyGrenadeFail = world.get_location("StD Police Chase Helicopter: Sticky Grenade Fail")
        world.set_rule(StDStickyGrenadeFail,Has("Sticky Grenade"))

        StDIntruderOnAScooter = world.get_location("StD: Intruder On A Scooter")
        world.set_rule(StDIntruderOnAScooter,Has("Tunisian Diamond"))
    
    if (use_ItA(world)):
        ItAZeroPointEnergyFail = world.get_location("ItA Cargo Bay: Zero-Point Energy Fail")
        world.set_rule(ItAZeroPointEnergyFail,Has("Zero-Point Energy"))

        ItABallNChainFail = world.get_location("ItA Cargo Bay: Ball 'n' Chain Fail")
        world.set_rule(ItABallNChainFail,Has("Ball 'n Chain"))

        ItABombFail = world.get_location("ItA Viewing Platform: Bomb Fail")
        world.set_rule(ItABombFail,Has("Bomb"))

        ItAJoyBuzzerFail = world.get_location("ItA Viewing Platform: Joy Buzzer Fail")
        world.set_rule(ItAJoyBuzzerFail,Has("Joy Buzzer"))

        ItAExpandingFoamFail = world.get_location("ItA Viewing Platform: Expanding Foam Fail")
        world.set_rule(ItAExpandingFoamFail,Has("Expanding Foam"))

        ItAStretchChewiesFail = world.get_location("ItA Engine Room Records Side: Stretch Chewies Fail")
        world.set_rule(ItAStretchChewiesFail,Has("Stretch Chewies"))

        ItAStretchChewiesFail = world.get_location("ItA Engine Room Records Side: Magic Pencil Fail")
        world.set_rule(ItAStretchChewiesFail,Has("Magic Pencil"))

        ItATeleporterFail = world.get_location("ItA Engine Room Records Side: Teleporter Fail")
        world.set_rule(ItATeleporterFail,Has("Teleporter"))

        ItAWizzardMagicFail = world.get_location("ItA Brig: Wizard Magic Fail")
        world.set_rule(ItAWizzardMagicFail,Has("Wizard Magic"))

        ItARetrogloveFail = world.get_location("ItA Brig: Retroglove Fail")
        world.set_rule(ItARetrogloveFail,Has("Retroglove"))

        ItAGravityManipulatorFail = world.get_location("ItA Vault: Gravity Manipulator Fail")
        world.set_rule(ItAGravityManipulatorFail,Has("Gravity Manipulator"))

        ItAClawpackFail = world.get_location("ItA Vault: Clawpack Fail")
        world.set_rule(ItAClawpackFail,Has("Clawpack"))

        ItAUmbrellaFail = world.get_location("ItA Outer Wing: Umbrella Fail")
        world.set_rule(ItAUmbrellaFail,Has("Umbrella"))

        ItAPropaneTankFail = world.get_location("ItA Outer Wing: Propane Tank Fail")
        world.set_rule(ItAPropaneTankFail,Has("Propane Tank"))

        ItAShellFail = world.get_location("ItA Outer Wing: Shell Fail")
        world.set_rule(ItAShellFail,Has("Shell"))

        ItADEBFail = world.get_location("ItA Center For Chaos Containment: D.E.B Fail")
        world.set_rule(ItADEBFail,Has("D.E.B Disk"))

        ItALKM2Fail = world.get_location("ItA Center For Chaos Containment: L. Cut mk. II Fail")
        world.set_rule(ItALKM2Fail,Has("L. Cut mk. II Disk"))

        ItGabenFail = world.get_location("ItA Center For Chaos Containment: Gaben Fail")
        world.set_rule(ItGabenFail,Has("Scratched Disk"))

        ItAPureBloodedTheif = world.get_location("ItA: Pure Blooded Thief")
        world.set_rule(ItAPureBloodedTheif,Has("Prototype Disk"))

        ItAAcidFail = world.get_location("ItA Airship Topside: Acid Fail")
        world.set_rule(ItAAcidFail,Has("Acid"))

        ItAC4Fail = world.get_location("ItA Airship Topside: C4 Fail")
        world.set_rule(ItAC4Fail,Has("C4"))

        ItADisguiseFail = world.get_location("ItA Boardroom: Disguise Fail")
        world.set_rule(ItADisguiseFail,Has("Toppat Disguise"))

        ItATransdimensionalizerFail = world.get_location("ItA Boardroom: Transdimensionalizer Fail")
        world.set_rule(ItATransdimensionalizerFail,Has("Transdimensionalizer"))

        ItAGravityBubbleFail = world.get_location("ItA Engine Room Vault Side: Gravity Bubble Fail")
        world.set_rule(ItAGravityBubbleFail,Has("Gravity Bubble"))

        ItAPlatformFail = world.get_location("ItA Engine Room Vault Side: Platform Fail")
        world.set_rule(ItAPlatformFail,Has("Platform"))

        ItAGatlingGunFail = world.get_location("ItA Engine Vents: Gatling Gun Fail")
        world.set_rule(ItAGatlingGunFail,Has("Gatling Gun"))

        ItAMindControlFail = world.get_location("ItA Engine Vents: Mind Control Fail")
        world.set_rule(ItAMindControlFail,Has("Mind Control"))

        ItARemoteAccessFail = world.get_location("ItA Engine Vents: Remote Access Fail")
        world.set_rule(ItARemoteAccessFail,Has("Remote Access"))

        ItANinjaStarFail = world.get_location("ItA Records Library: Ninja Star Fail")
        world.set_rule(ItANinjaStarFail,Has("Ninja Star"))

        ItAFalconKickFail = world.get_location("ItA Records Library: Falcon Kick Fail")
        world.set_rule(ItAFalconKickFail,Has("Falcon Kick"))

        ItABananaBombFail = world.get_location("ItA Cargo Bay Evidence: Banana Bomb Fail")
        world.set_rule(ItABananaBombFail,Has("Banana Bomb"))
        
        ItASleepingGasFail = world.get_location("ItA Cargo Bay Evidence: Sleeping Gas Fail")
        world.set_rule(ItASleepingGasFail,Has("Sleeping Gas"))

        ItAFlashbangFail = world.get_location("ItA Cargo Bay Evidence: Flashbang Fail")
        world.set_rule(ItAFlashbangFail,Has("Flashbang"))

        ItAGovermentSupportedPrivateInvestagator = world.get_location("ItA: Government Supported Private Investigator")
        world.set_rule(ItAGovermentSupportedPrivateInvestagator,Has("Force Gun"))

        ItALaserFail = world.get_location("ItA Bridge: Laser Fail")
        world.set_rule(ItALaserFail,Has("Cannon Ball Laser"))

        ItAThrusterFail = world.get_location("ItA Bridge: Thruster Fail")
        world.set_rule(ItAThrusterFail,Has("Cannon Ball Thruster"))

        ItASpikesFail = world.get_location("ItA Warehouse: Spikes Fail")
        world.set_rule(ItASpikesFail,Has("Cannon Ball Spikes"))

        ItABoostFail = world.get_location("ItA Warehouse: Boost Fail")
        world.set_rule(ItABoostFail,Has("Cannon Ball Boost"))

        ItAWarpFail = world.get_location("ItA Quarters Hallway: Warp Fail")
        world.set_rule(ItAWarpFail,Has("Warp"))

        ItAMetalFistFail = world.get_location("ItA Quarters Hallway: Metal Fist Fail")
        world.set_rule(ItAMetalFistFail,Has("Metal Fist"))

        ItARoboPantsFail = world.get_location("ItA Brig Damaged: Robo Pants Fail")
        world.set_rule(ItARoboPantsFail,Has("Robo Pants"))   

        ItAMetalbendFail = world.get_location("ItA Brig Damaged: Metal Bend Fail")
        world.set_rule(ItAMetalbendFail,Has("Metalbending"))

        ItAPSIFail = world.get_location("ItA Yo-Yo Fight: PSI Fail")
        world.set_rule(ItAPSIFail,Has("PSI Flash"))

        ItAFireMagicFail = world.get_location("ItA Dirk Fight: Magic Fail")
        world.set_rule(ItAFireMagicFail,Has("Fire Magic"))

        ItAJetbootsFail = world.get_location("ItA Ventalation Shaft: JetBoots Fail")
        world.set_rule(ItAJetbootsFail,Has("JetBoots"))       

        ItABeefUpFail = world.get_location("ItA Ventalation Shaft: Beef Up Fail")
        world.set_rule(ItABeefUpFail,Has("Beef Up"))

        ItAParachuteFail = world.get_location("ItA Cargo Bay Hostage: Parachute Fail")
        world.set_rule(ItAParachuteFail,Has("Parachute"))

        ItAMissileFail = world.get_location("ItA Cargo Bay Hostage: Missile Fail")
        world.set_rule(ItAMissileFail,Has("Missile"))

        ItARapidlyPromotedExecutive = world.get_location("ItA: Rapidly Promoted Executive")
        world.set_rule(ItARapidlyPromotedExecutive,Has("Dummies"))

        ItARelentlessBountyHunter = world.get_location("ItA: Relentlesss Bounty Hunter")
        world.set_rule(ItARelentlessBountyHunter,Has("Tank"))

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
