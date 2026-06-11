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


class Goal(Choice):
    """
    What do you have to achive to beat the game (obviously 1 doesen't work right now because those games aren't yet supported)
    0 - Achive a certain amount of ranks across all henry games
    1 - Achive any rank in CtM this obviously requires at least one ending in FtC and ItA as well
    2 - Achive any rank in each of the games included in the randomization
    """
    display_name = "Goal"
    option_rank_hunt = 0
    option_complete_the_mission = 1
    option_complete_every_mission = 2
    default = 0

class Required_Ranks(Range):
    "How many ranks must you achive does nothing if goal is not rank hunt.  If you are not including all games in the randomization make sure this option is set to less than the number of ranks in all the games you include"
    range_start = 1
    range_end = 4

class Teleporter_Start(Choice):
    """
    Start with a teleporter if you don't do this or give another item you will start off BKed and generation will fail in singleplayer
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
