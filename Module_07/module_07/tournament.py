from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (BattleStrategy, NormalStrategy,
                 AggressiveStrategy, DefensiveStrategy,
                 CreatureStrategyMismatchError)


def battle(items: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    new_items = [(x.create_base(), y) for x, y in items]

    print("*** Tournament ***")
    print(f"{(n := len(items))} opponents involved")
    for i in range(n - 1):
        for j in range(i + 1, n):
            print("\n* Battle *")
            x, sx = new_items[i]
            y, sy = new_items[j]
            print(x.describe())
            print(" vs.")
            print(y.describe())
            print(" now fight!")
            try:
                for pair in [(x, sx), (y, sy)]:
                    if not isinstance(pair[1], DefensiveStrategy):
                        pair[1].act(pair[0])
                    else:
                        # free-for-all battle
                        pair[1].act(pair[0], [pair[0]])
            except CreatureStrategyMismatchError as error:
                print(error)
                return


if __name__ == "__main__":
    strategy = [NormalStrategy(), AggressiveStrategy(), DefensiveStrategy()]
    factory = [FlameFactory(), AquaFactory(), HealingCreatureFactory(),
               TransformCreatureFactory()]

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    fight = [(factory[0], strategy[0]), (factory[2], strategy[2])]
    battle(fight)

    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    fight = [(factory[0], strategy[1]), (factory[2], strategy[2])]
    battle(fight)

    print("Tournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    fight = [(factory[1], strategy[0]), (factory[2], strategy[2]),
             (factory[3], strategy[1])]
    battle(fight)
