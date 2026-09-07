from sys import argv


def ft_items(d: dict[str, int]) -> list[tuple[str, int]]:
    return [(x, d[x]) for x in d]


def ft_max(items: list[tuple[str, int]]) -> tuple[str, int]:
    best = items[0]
    for item in items[1:]:
        if item[1] > best[1]:
            best = item
    return best


def ft_min(items: list[tuple[str, int]]) -> tuple[str, int]:
    best = items[0]
    for item in items[1:]:
        if item[1] < best[1]:
            best = item
    return best


def create_dict() -> dict[str, int]:

    dargv: dict[str, int] = {}
    nargv = argv[1:]

    if not nargv:
        print("Error - Missing parameters")
        return dargv

    for x in nargv:
        if not ((":" in x) and (x.count(":") == 1)):
            print(f"Error - invalid parameter \'{x}\'")
            continue
        if not (key := x[:x.find(":")]).isalpha():
            print(f"Invalid item \'{key}\' - discarding")
            continue
        if key in dargv.keys():
            print(f"Redundant item \'{key}\' - discarding")
            continue
        if not (value := x[x.find(":") + 1:]).isdecimal():
            print(f"Quantity error for '{key}': value must"
                  f" be a non-negative integer: '{value}'")
            continue
        dargv |= {key: int(value)}      # 1. in-place
        # 2. dargv.update({key: int(value)}) in-place
        # 3. dargv = {**dargv, **{key: int(value)}}

    if not sum(dargv.values()):
        print("Quantity error: at least one quantity must be non-zero")
        return {}
    return dargv


def inventory_analysis() -> None:
    if not (dargv := create_dict()):
        return print("Error - Missing valid parameters")
    print(f"Got inventory: {dargv}")
    print(f"Item list: {list(dargv.keys())}")
    print(f"Total quantity of the {len(dargv)} items: "
          f"{(sum_valus := sum(dargv.values()))}")
    for x, y in (dict_items := ft_items(dargv)):
        print(f"Item {x} represents {y / sum_valus * 100:.1f}%")
    print("Item most abundant: "
          f"{(tupla_max := ft_max(dict_items))[0]}"
          f" with quantity {tupla_max[1]}")
    print("Item least abundant: "
          f"{(tupla_min := ft_min(dict_items))[0]}"
          f" with quantity {tupla_min[1]}")
    print(f"Updated inventory: {dargv.update({'magic_item': 1}) or dargv}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory_analysis()
