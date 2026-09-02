from dataclasses import dataclass

from Options import Choice, PerGameCommonOptions, Range

# https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/options%20api.md



class BtB(Choice):
    """
    Include Henry Stickmin Breaking the Bank in the randomization
    0 - Don't include Breaking the Bank
    1 - include Breaking the Bank its avilable from the start
    2 - include Breaking the Bank its unlocked when you receve it from an archipelago check
    """
    display_name = "Breaking the Bank"
    option_no = 0
    option_yes_open_world = 1
    option_yes_multiworld = 2
    default = 1


class EtP(Choice):
    """
    Include Henry Stickmin Escaping the Prison in the randomization
    0 - Don't include Escaping the Prison
    1 - include Escaping the Prison its avilable from the start
    2 - include Escaping the Prison its unlocked when you receve it from an archipelago check
    3 - include Escaping the Prison its unlocked when you complete Breaking the Bank

    """
    display_name = "Escaping the Prison"
    option_no = 0
    option_yes_open_world = 1
    option_yes_multiworld = 2
    option_yes_vanilla = 3
    default = 1

class StD(Choice):
    """
    Include Henry Stickmin Stealing the Diamond in the randomization
    0 - Don't include Stealing the Diamond
    1 - include Stealing the Diamond its avilable from the start
    2 - include Stealing the Diamond its unlocked when you receve it from an archipelago check
    3 - include Stealing the Diamond its unlocked when you complete any rank in Escaping the Prison

    """
    display_name = "Stealing the Diamond"
    option_no = 0
    option_yes_open_world = 1
    option_yes_multiworld = 2
    option_yes_vanilla = 3
    default = 1

class ItA(Choice):
    """
    Include Henry Stickmin Infiltrating the Airship in the randomization
    0 - Don't include Infiltrating the Airship
    1 - include Infiltrating the Airship its avilable from the start
    2 - include Infiltrating the Airship its unlocked when you receve it from an archipelago check
    3 - include Infiltrating the Airship its unlocked when you complete any rank in Stealing the Diamond

    """
    display_name = "Infiltrating the Airship"
    option_no = 0
    option_yes_open_world = 1
    option_yes_multiworld = 2
    option_yes_vanilla = 3
    default = 1

class FtC(Choice):
    """
    Include Henry Stickmin Fleeing the Complex in the randomization
    0 - Don't include Fleeing the Complex
    1 - include Fleeing the Complex its avilable from the start
    2 - include Fleeing the Complex its unlocked when you receve it from an archipelago check
    3 - include Fleeing the Complex its unlocked when you complete any rank in Infiltrating the Airship

    """
    display_name = "Fleeing the Complex"
    option_no = 0
    option_yes_open_world = 1
    option_yes_multiworld = 2
    option_yes_vanilla = 3
    default = 1

class FtCPhoneAFriendMode(Choice):
    """
    How Should the Phone a friend event be handled in Fleeing the complex
    0 - Vanilla unlock the phone a friend options when you complete rapidly promoted excutive and either relentless bounty hunter or goverment supported private investagator
    1 - Phone numbers unlock the options by collecting "Charles's Phone Number" and "Reginald's Phone Number" from the multiworld this option is always used if Infiltrating the Airship is not enabled
    """
    display_name = "Phone a friend mode"
    option_vanilla = 0
    option_phone_numbers = 1
    default = 0


class CtM(Choice):
    """
    Include Henry Stickmin Completing the Mission in the randomization
    0 - Don't include Completing the Mission
    1 - include Completing the Mission its avilable from the start
    2 - include Completing the Mission its unlocked when you receve it from an archipelago check
    3 - include Completing the Mission its unlocked when you complete any rank in Fleeing the Complex

    """
    display_name = "Completing the Missionx"
    option_no = 0
    option_yes_open_world = 1
    option_yes_multiworld = 2
    option_yes_vanilla = 3
    default = 1

class CtMTimelineUnlockMode(Choice):
    """
    How Should the Timelines be unlocked for Completing the Mission
    0 - Vanilla unlock the timelines by completing the endings in FtC and ItA
    1 - Timeline Items unlock the options by collecting timeline items from the multiworld (ie "Presumed Dead Timeline") this option is always used if Infiltrating the Airship or Fleeing the Complex are not enabled (if only one is enabled and this is set to vanilla you will use vanilla progression to get the timelines from the enabled game and timeline items for the disabled game)
    2 - Open World all timelines are unlocked from the begining you just have to unlock CtM
    """
    display_name = "Timeline Unlock Mode"
    option_vanilla = 0
    option_timeline_items = 1
    option_open_world = 2
    default = 0



class Goal(Choice):
    """
    What do you have to achive to beat the game (obviously 1 doesen't work right now because CtM isen't yet supported)
    0 - Achive a certain amount of ranks across all henry games
    1 - Achive any rank in CtM this obviously requires at least one timeline unlocked from both ItA and FtC (if CtM is disabled and this option is picked it will default to complete every mission instead)
    2 - Achive any rank in each of the games included in the randomization
    """
    display_name = "Goal"
    option_rank_hunt = 0
    option_complete_the_mission = 1
    option_complete_every_mission = 2
    default = 0

class Required_Ranks(Range):
    "How many ranks must you achive does nothing if goal is not rank hunt.  If you are not including all games in the randomization and this is set higher than the total acivable ranks for the games you have your goal will become achive all ranks"
    range_start = 1
    range_end = 32
    default = 12

class Teleporter_Start(Choice):
    """
    Start with a teleporter 
    if you don't do this, give another item or start with StD or FtC you will start off BKed and generation will fail in singleplayer
    """
    option_no = 0
    option_yes = 1
    default = 0



# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class HenryStickminOptions(PerGameCommonOptions):
    BtB: BtB
    EtP: EtP
    StD: StD
    ItA: ItA
    FtC: FtC
    CtM: CtM
    FtCPhoneAFriendMode:FtCPhoneAFriendMode
    CtMTimelineUnlockMode:CtMTimelineUnlockMode
    Goal: Goal
    Required_Ranks: Required_Ranks
    Teleporter_Start: Teleporter_Start


# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
# option_groups = [
#     OptionGroup(
#         "Gameplay Options",
#         [HardMode, Hammer, ExtraStartingChest, StartWithOneConfettiCannon, TrapChance],
#     ),
#     OptionGroup(
#         "Aesthetic Options",
#         [ConfettiExplosiveness, PlayerSprite],
#     ),
# ]

# Finally, we can define some option presets if we want the player to be able to quickly choose a specific "mode".
# option_presets = {
#     "boring": {
#         "hard_mode": False,
#         "hammer": False,
#         "extra_starting_chest": False,
#         "start_with_one_confetti_cannon": False,
#         "trap_chance": 0,
#         "confetti_explosiveness": ConfettiExplosiveness.range_start,
#         "player_sprite": PlayerSprite.option_human,
#     },
#     "the true way to play": {
#         "hard_mode": True,
#         "hammer": True,
#         "extra_starting_chest": True,
#         "start_with_one_confetti_cannon": True,
#         "trap_chance": 50,
#         "confetti_explosiveness": ConfettiExplosiveness.range_end,
#         "player_sprite": PlayerSprite.option_duck,
#     },
# }
