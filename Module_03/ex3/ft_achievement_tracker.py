import random as r


# --------------------------------------------------------------
class SetOperation:
    def __call__(self, a: set[str], b: set[str]) -> set[str]:
        return a


class UnionOperation(SetOperation):
    def __call__(self, a: set[str], b: set[str]) -> set[str]:
        return set.union(a, b)


class IntersectionOperation(SetOperation):
    def __call__(self, a: set[str], b: set[str]) -> set[str]:
        return set.intersection(a, b)  # a & b
# --------------------------------------------------------------
# alternatively (more performance):
# class SetOperation:
#     def __call__(self, *args: set[str]) -> set[str]:
#         return args
#
#
# class UnionOperation(SetOperation):
#     def __call__(self, *args: set[str]) -> set[str]:
#         return set.union(*args)
#
#
# class IntersectionOperation(SetOperation):
#     def __call__(self, *args: set[str]) -> set[str]:
#         return set.intersection(*args)


def gen_player_achievements(achievements: list[str]) -> set[str]:
    n_max = len(achievements)
    n_player_chts = r.randint(int(n_max * 4 / 10), int(n_max * 7 / 10))
    player_chts: set[str] = set()
    while True:
        if len(player_chts) == n_player_chts:
            return player_chts
        player_chts |= {r.choice(achievements)}      # 1. in-place
        # 2. player_chts.update({r.choice(achievements)}) in-place
        # 3. player_chts = {*player_chts, r.choice(achievements)}
        # 4. player_chts = player_chts.union({r.choice(achievements)})


def print_player_achievements(player: str, player_chts: set[str]) -> None:
    print(f"Player {player}: {player_chts}")


def print_m_achievements(list_chts: list[set[str]], m: SetOperation,
                         message: str) -> None:
    # --------------------------------------------------------------
    f_achieve = list_chts[0]
    for x in list_chts:
        f_achieve = m(f_achieve, x)
    # --------------------------------------------------------------
    # alternatively (more performance) with uncomment lines 18 through 32:
    # f_achieve = m(*list_chts)
    print(f"\n{message} achievements: {f_achieve}")


def print_difference_achievements(list_name: list[str],
                                  list_chts: list[set[str]]) -> None:
    i = 0
    print()
    for x in list_chts:
        # ----------------------------------------------------------
        for y in list_chts[i + 1:] + list_chts[:i]:
            x = x - y
            # no x.difference_update(y) in-place
            # ok x = x.difference(y)
        # ----------------------------------------------------------
        # alternatively (more performance):
        # list_achieve_without_x = list_chts[i + 1:] + list_chts[:i]
        # 1. x = x.difference(*list_achieve_without_x)
        # 2. x = x - set().union(*list_achieve_without_x)
        print(f"Only {list_name[i]} has: {x}")
        i += 1


def print_missing_achievements(list_name: list[str], list_chts: list[set[str]],
                               achievements: list[str]) -> None:
    i = 0
    print()
    for x in list_chts:
        print(f"{list_name[i]} is missing: {set(achievements).difference(x)}")
        i += 1


def play_achievement_tracker_system(list_name: list[str],
                                    achievements: list[str]) -> None:
    list_chts: list[set[str]] = []
    for name in list_name:
        list_chts += [gen_player_achievements(achievements)]
        print_player_achievements(name, list_chts[len(list_chts) - 1])
    print_m_achievements(list_chts, UnionOperation(), "All distinct")
    print_m_achievements(list_chts, IntersectionOperation(), "Common")
    print_difference_achievements(list_name, list_chts)
    print_missing_achievements(list_name, list_chts, achievements)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    name_players = ["Alice", "Bob", "Charlie", "Dylan"]
    achievements = ['Crafting Genius', 'Strategist', 'World Savior',
                    'Speed Runner', 'Survivor', 'Master Explorer',
                    'Treasure Hunter', 'Unstoppable', 'First Steps',
                    'Collector Supreme', 'Untouchable', 'Sharp Mind',
                    'Boss Slayer']
    play_achievement_tracker_system(name_players, achievements)
