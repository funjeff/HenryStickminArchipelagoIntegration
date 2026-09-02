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
    
    if use_FtC(world):
        ftcTransferCell = Region("ftcTransferCell", world.player, world.multiworld)

        ftcTheYardTactical = Region("ftcTheYardTactical", world.player, world.multiworld)
        ftcBehindTheTruck = Region("ftcBehindTheTruck", world.player, world.multiworld)
        ftcCarChase = Region("ftcCarChase", world.player, world.multiworld)

        ftcCafeteriaGovernment = Region("ftcCafeteriaGovernment", world.player, world.multiworld)
        ftcFireEscape = Region("ftcFireEscape", world.player, world.multiworld)
        ftcHelipad = Region("ftcHelipad", world.player, world.multiworld)

        ftcCafeteriaToppat = Region("ftcCafeteriaToppat", world.player, world.multiworld)
        ftcAirship = Region("ftcAirship", world.player, world.multiworld)

        ftcOutsideSecuritySolo = Region("ftcOutsideSecuritySolo", world.player, world.multiworld)
        ftcElevator = Region("ftcElevator", world.player, world.multiworld)
        ftcBowelsOfTheComplex = Region("ftcBowelsOfTheComplex", world.player, world.multiworld)
        ftcDocks = Region("ftcDocks", world.player, world.multiworld)
        ftcOuterDocks = Region("ftcOuterDocks", world.player, world.multiworld)

        ftcHallwayStandoff = Region("ftcHallwayStandoff", world.player, world.multiworld)
        ftcTwoElevators = Region("ftcTwoElevators", world.player, world.multiworld)
        ftcTheYardCaptured = Region("ftcTheYardCaptured", world.player, world.multiworld)

        ftcRegions = [ftcTransferCell,ftcTheYardTactical,ftcBehindTheTruck,ftcCarChase,ftcCafeteriaGovernment,ftcFireEscape,ftcHelipad,ftcCafeteriaToppat,ftcAirship,ftcOutsideSecuritySolo,ftcElevator,ftcBowelsOfTheComplex,ftcDocks,ftcOuterDocks,ftcHallwayStandoff,ftcTwoElevators,ftcTheYardCaptured]
        regions.extend(ftcRegions)
    
    if use_CtM(world):
        # toppat king
        ctmControlTower = Region("ctmControlTower", world.player, world.multiworld)
        ctmInsideHelicopter = Region("ctmInsideHelicopter", world.player, world.multiworld)
        ctmUnderTheRocket = Region("ctmUnderTheRocket", world.player, world.multiworld)
        ctmBackToBack = Region("ctmBackToBack", world.player, world.multiworld)
        ctmDrivingUpTheRamp = Region("ctmDrivingUpTheRamp", world.player, world.multiworld)
        
        #Free Man
        ctmOrbitalCell = Region("ctmOrbitalCell", world.player, world.multiworld)
        ctmOrbitalCellStill = Region("ctmOrbitalCellStill", world.player, world.multiworld)
        ctmChooseYourWeapon = Region("ctmChooseYourWeapon", world.player, world.multiworld)
        ctmCafeteriaSpace = Region("ctmCafeteriaSpace", world.player, world.multiworld)
        ctmSolarPanelDash = Region("ctmSolarPanelDash", world.player, world.multiworld)
        ctmEscapePlan = Region("ctmEscapePlan", world.player, world.multiworld)

        #Special BROvert Ops
        ctmSAMTurretRoof = Region("ctmSAMTurretRoof", world.player, world.multiworld)
        ctmCrossOver = Region("ctmCrossOver", world.player, world.multiworld)
        ctmStorageBayCharles = Region("ctmStorageBayCharles", world.player, world.multiworld)
        ctmEngineRoom = Region("ctmEngineRoom", world.player, world.multiworld)
        ctmHallOfLeaders = Region("ctmHallOfLeaders", world.player, world.multiworld)
        ctmCockpit = Region("ctmCockpit", world.player, world.multiworld)

        #Triple Threat
        ctmWhereWeDroppin = Region("ctmWhereWeDroppin", world.player, world.multiworld)
        ctmRocketBoardingLastCall = Region("ctmRocketBoardingLastCall", world.player, world.multiworld)
        ctmComboTime = Region("ctmComboTime", world.player, world.multiworld)
        ctmCafeteriaJungle = Region("ctmCafeteriaJungle", world.player, world.multiworld)
        
        #Stickmin Space Resort
        ctmJungleTrail = Region("ctmJungleTrail", world.player, world.multiworld)
        ctmTopOfTheRocket = Region("ctmTopOfTheRocket", world.player, world.multiworld)
        ctmTethered = Region("ctmTethered", world.player, world.multiworld)

        #Jewel Baron
        ctmSpaceScooter = Region("ctmSpaceScooter", world.player, world.multiworld)
        ctmGravityPit = Region("ctmGravityPit", world.player, world.multiworld)
        ctmStationVault = Region("ctmStationVault", world.player, world.multiworld)
        ctmSecretWeapon = Region("ctmSecretWeapon", world.player, world.multiworld)

        #Little Nest Egg
        ctmTankAttack = Region("ctmTankAttack",world.player, world.multiworld)
        ctmTraintopSprint = Region("ctmTraintopSprint",world.player, world.multiworld)
        ctmGetawayMeans = Region("ctmGetawayMeans",world.player, world.multiworld)

        #Pardoned Pals/Toppat Recruits
        ctmParkingLot = Region("ctmParkingLot",world.player, world.multiworld)
        ctmLaunchTowerHallway = Region("ctmLaunchTowerHallway",world.player, world.multiworld)
        ctmCollapse = Region("ctmCollapse",world.player, world.multiworld)
        ctmFactionFriction = Region("ctmFactionFriction",world.player, world.multiworld)

        #Toppat 4 Life
        ctmCliffside = Region("ctmCliffside",world.player, world.multiworld)
        ctmTheWatchtower = Region("ctmTheWatchtower",world.player, world.multiworld)
        ctmBigBoy = Region("ctmBigBoy",world.player, world.multiworld)
        ctmCCCMobileUnit = Region("ctmCCCMobileUnit",world.player, world.multiworld)

        #Cleaned 'em Out
        ctmCargoStopped = Region("ctmCargoStopped",world.player, world.multiworld)
        ctmPassangerCar = Region("ctmPassangerCar",world.player, world.multiworld)
        ctmStorageBay = Region("ctmStorageBay",world.player, world.multiworld)

        #Master Bounty Hunter
        ctmFrontGate = Region("ctmFrontGate",world.player, world.multiworld)
        ctmDoorway = Region("ctmDoorway",world.player, world.multiworld)
        ctmBountysFate = Region("ctmBountysFate",world.player, world.multiworld)

        #Valliant Hero
        ctmInfiltratingTheOrbitalStation = Region("ctmInfiltratingTheOrbitalStation",world.player, world.multiworld)
        ctmOrbitalHull = Region("ctmOrbitalHull",world.player, world.multiworld)

        #Toppat Civil Warfare
        ctmThePlank = Region("ctmThePlank",world.player, world.multiworld)
        ctmTheBrig = Region("ctmTheBrig",world.player, world.multiworld)

        #Capital Gains
        ctmTrainAssault = Region("ctmTrainAssault",world.player, world.multiworld)
        ctmCrashSite = Region("ctmCrashSite",world.player, world.multiworld)
        ctmFloatingCart = Region("ctmFloatingCart",world.player, world.multiworld)

        #Revenged
        ctmShowdown = Region("ctmShowdown",world.player, world.multiworld)
        ctmFinishingMove = Region("ctmFinishingMove",world.player, world.multiworld)
        ctmClaimRevenge = Region("ctmClaimRevenge",world.player, world.multiworld)

        ctmRegions = [ctmControlTower,ctmInsideHelicopter,ctmUnderTheRocket,ctmBackToBack,ctmDrivingUpTheRamp,ctmOrbitalCell,ctmOrbitalCellStill,ctmChooseYourWeapon,ctmCafeteriaSpace,ctmSolarPanelDash,ctmEscapePlan,ctmSAMTurretRoof,ctmCrossOver,ctmStorageBayCharles,ctmEngineRoom,ctmHallOfLeaders,ctmCockpit,ctmWhereWeDroppin,ctmRocketBoardingLastCall,ctmComboTime,ctmCafeteriaJungle,ctmJungleTrail,ctmTopOfTheRocket,ctmTethered,ctmSpaceScooter,ctmGravityPit,ctmStationVault,ctmSecretWeapon,ctmTankAttack,ctmTraintopSprint,ctmGetawayMeans,ctmParkingLot,ctmLaunchTowerHallway,ctmCollapse,ctmFactionFriction,ctmCliffside,ctmTheWatchtower,ctmBigBoy,ctmCCCMobileUnit,ctmCargoStopped,ctmPassangerCar,ctmStorageBay,ctmFrontGate,ctmDoorway,ctmBountysFate,ctmInfiltratingTheOrbitalStation,ctmOrbitalHull,ctmThePlank,ctmTheBrig,ctmTrainAssault,ctmCrashSite,ctmFloatingCart,ctmShowdown,ctmFinishingMove,ctmClaimRevenge]
        regions.extend(ctmRegions)
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
    
    if use_FtC(world):
        create_region_progression(world,chapterSelect,["ftcTransferCell","ftcTheYardTactical","ftcBehindTheTruck","ftcCarChase"],[get_FtC_unlock_rule(world),Has("Item Box"),Has("Sword"),Has("Wall Truck Keys")],"FtC Presumed Dead Progression")
        ftcTransferCell = world.get_region("ftcTransferCell")
        
        if use_ItA(world) and world.options.FtCPhoneAFriendMode == 0:
            phoneAFriendCharlesRule = Has("Relentless Bounty Hunter Event Item") | Has("Government Supported Private Investigator Event Item")
        else:
            phoneAFriendCharlesRule = Has("Charles's Phone Number")
        
        create_region_progression(world,ftcTransferCell,["ftcCafeteriaGovernment","ftcFireEscape","ftcHelipad"],[Has("Laser Plane") & phoneAFriendCharlesRule,Has("Flash"),Has("Mini Helicopter")],"FtC International Rescue Operative Progression")
        
        if use_ItA(world) and world.options.FtCPhoneAFriendMode == 0:
            phoneAFriendReginaldRule = Has("Rapidly Promoted Executive Event Item")
        else:
            phoneAFriendReginaldRule = Has("Reginald's Phone Number")

        create_region_progression(world,ftcTransferCell,["ftcCafeteriaToppat","ftcAirship"],[Has("Laser Plane") & phoneAFriendReginaldRule,Has("Drill Pod")],"FtC The Betrayed Progression")
       
        create_region_progression(world,ftcTransferCell,["ftcOutsideSecuritySolo","ftcElevator","ftcBowelsOfTheComplex","ftcDocks","ftcOuterDocks"],[Has("Whoopee Cushion"),Has("Power Jump"),Has("Balloon"),Has("Helium"),Has("Super Leaf")],"FtC Ghost Inmate Progression")
        create_region_progression(world,ftcTransferCell,["ftcHallwayStandoff","ftcTwoElevators","ftcTheYardCaptured"],[Has("The Force"),Has("Taser") & Has("Sniper Rifle"),Has("The Wall Hat")],"FtC Convict Allies Progression")
    
    if use_CtM(world):
        create_region_progression(world,chapterSelect,["ctmControlTower","ctmInsideHelicopter","ctmUnderTheRocket","ctmBackToBack","ctmDrivingUpTheRamp"],[get_CtM_timeline_unlock_rule(world,"Rapidly Promoted Executive","Convict Allies"),Has("Wrist Strapped Grapple Hook"),Has("Mounted Gun"),Has("Flute"),Has("Dual Tech")],"CtM Toppat King Progression")
        create_region_progression(world,chapterSelect,["ctmOrbitalCell","ctmOrbitalCellStill","ctmChooseYourWeapon","ctmCafeteriaSpace","ctmSolarPanelDash","ctmEscapePlan"],[get_CtM_timeline_unlock_rule(world,"Relentless Bounty Hunter","Ghost Inmate"),Has("Thunder II"),Has("Metal Hat"),Has("Pew Pew Gun"),Has("Nano-Suit"),Has("Max Gravity Boots")],"CtM Free Man Progression")
        create_region_progression(world,chapterSelect,["ctmSAMTurretRoof","ctmCrossOver","ctmStorageBayCharles","ctmEngineRoom","ctmHallOfLeaders","ctmCockpit"],[get_CtM_timeline_unlock_rule(world,"Government Supported Private Investigator","International Rescue Operative"),Has("Drawing"),Has("Trapeze"),Has("Remote Toppat"),Has("Red Herring"),Has("Swapper")],"CtM Special BROvert Ops Progression")
        create_region_progression(world,chapterSelect,["ctmWhereWeDroppin","ctmRocketBoardingLastCall","ctmComboTime","ctmCafeteriaJungle"],[get_CtM_timeline_unlock_rule(world,"Government Supported Private Investigator","Convict Allies"),Has("JetPack"),Has("Barrel"),Has("Human Cannon")],"CtM Tripple Threat Progression")
        create_region_progression(world,chapterSelect,["ctmJungleTrail","ctmTopOfTheRocket","ctmTethered"],[get_CtM_timeline_unlock_rule(world,"Pure Blooded Thief","Presumed Dead"),Has("Spiked Wheels"),Has("Hammer")],"CtM Stickmin Space Resort Progression")
        create_region_progression(world,chapterSelect,["ctmSpaceScooter","ctmGravityPit","ctmStationVault","ctmSecretWeapon"],[get_CtM_timeline_unlock_rule(world,"Pure Blooded Thief","Ghost Inmate"),Has("Mosquito Mode"),Has("Teleporter"),Has("Rah Doh FOO")],"CtM Jewel Baron Progression")
        create_region_progression(world,chapterSelect,["ctmTankAttack","ctmTraintopSprint","ctmGetawayMeans"],[get_CtM_timeline_unlock_rule(world,"Relentless Bounty Hunter","Presumed Dead"),Has("Tank"),Has("Mirror")],"CtM Little Nest Egg Progression")
        create_region_progression(world,chapterSelect,["ctmParkingLot","ctmLaunchTowerHallway","ctmCollapse","ctmFactionFriction"],[get_CtM_timeline_unlock_rule(world,"Pure Blooded Thief","Convict Allies"),Has("Rope") & Has("Wings"),Has("Time Machine"),Has("Block")],"CtM Pardoned Pals Progression")
        create_region_progression(world,chapterSelect,["ctmCliffside","ctmTheWatchtower","ctmBigBoy","ctmCCCMobileUnit"],[get_CtM_timeline_unlock_rule(world,"Rapidly Promoted Executive","Presumed Dead"),Has("Glitchy Physics Engine"),Has("Lagswitch"),Has("Scrambler")],"CtM Toppat 4 Life Progression")
        create_region_progression(world,chapterSelect,["ctmCargoStopped","ctmPassangerCar","ctmStorageBay"],[get_CtM_timeline_unlock_rule(world,"Government Supported Private Investigator","Ghost Inmate"),Has("Magic Hat"),Has("Free Transform")],"CtM Cleaned 'em Out Progression")
        create_region_progression(world,chapterSelect,["ctmFrontGate","ctmDoorway","ctmBountysFate"],[get_CtM_timeline_unlock_rule(world,"Relentless Bounty Hunter","International Rescue Operative"),Has("Woolooloo"),Has("Cheap Fighting Combo")],"CtM Master Bounty Hunter Progression")
        create_region_progression(world,chapterSelect,["ctmInfiltratingTheOrbitalStation","ctmOrbitalHull"],[get_CtM_timeline_unlock_rule(world,"Government Supported Private Investigator","Presumed Dead"),Has("Trash Ball")],"CtM Valliant Hero Progression")
        create_region_progression(world,chapterSelect,["ctmThePlank","ctmTheBrig"],[get_CtM_timeline_unlock_rule(world,"Rapidly Promoted Executive","Ghost Inmate"),Has("Helicopter Hat")],"CtM Toppat Civil Warfare Progression")
        create_region_progression(world,chapterSelect,["ctmTrainAssault","ctmCrashSite","ctmFloatingCart"],[get_CtM_timeline_unlock_rule(world,"Relentless Bounty Hunter","Convict Allies"),Has("Tank"),Has("Fulton")],"CtM Capital Gains Progression")
        create_region_progression(world,chapterSelect,["ctmShowdown","ctmFinishingMove","ctmClaimRevenge"],[get_CtM_timeline_unlock_rule(world,"Rapidly Promoted Executive","The Betrayed"),Has("Blade Forme"),Has("Y-Type Move")],"CtM Revenged Progression")
