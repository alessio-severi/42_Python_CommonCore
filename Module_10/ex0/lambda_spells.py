from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]
                    ) -> list[dict[str, Any]]:
    li = list(filter(lambda x: x.get('power') is not None, artifacts))
    return sorted(li, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict[str, Any]], min_power: int
                 ) -> list[dict[str, Any]]:
    return list(filter(lambda x: (x.get('power') is not None)
                       and x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict[str, Any]]
               ) -> dict[str, int | float]:
    k: list[dict[str, int | float]] = [{'power': power} for x in mages if (
            isinstance(power := x.get('power'), (int, float)))]
    return {'max_power': d['power'] if isinstance(d := max(k, default=float(
                'nan'), key=(f := lambda x: x['power'])), dict) else d,
            'min_power': d['power'] if isinstance(d := min(k, default=float(
                'nan'), key=f), dict) else d,
            'avg_power': (round(sum(map(lambda x: x['power'], k)) / len(
                k), ndigits=2) if isinstance(d, dict) else d)}


if __name__ == "__main__":
    artifacts = [{'name': 'Light Prism', 'power': 116, 'type': 'accessory'},
                 {'name': 'Lightning Rod', 'power': 97, 'type': 'focus'},
                 {'name': 'Wind Cloak', 'power': 77, 'type': 'accessory'},
                 {'name': 'Earth Shield', 'power': 95, 'type': 'armor'}]
    mages = [{'name': 'Riley', 'power': 84, 'element': 'ice'},
             {'name': 'Nova', 'power': 83, 'element': 'ice'},
             {'name': 'Riley', 'power': 85, 'element': 'water'},
             {'name': 'Alex', 'power': 78, 'element': 'light'},
             {'name': 'Sage', 'power': 91, 'element': 'fire'}]
    spells = ['meteor', 'earthquake', 'blizzard', 'flash']

    print("\nTesting artifact sorter...")
    print(f"Artifact list ordered by power: {artifact_sorter(artifacts)}")

    print("\nTesting power filter...")
    print(power_filter(mages, 84))

    print("\nTesting spell transformer...")
    print(" ".join(res) if (res := spell_transformer(spells)) else [])

    print("\nTesting mage stats...")
    print(mage_stats(mages))
