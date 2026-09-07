from math import sqrt


def get_coordinates() -> tuple[float, float, float]:
    def try_get_coordinates() -> tuple:
        def try_get_coordinate(str_arg: str) -> float | None:
            try:
                return float(str_arg)
            except ValueError:
                return print(f"Error on parameter \'{str_arg}\': could not"
                             f" convert string to float: \'{str_arg}\'")

        n_str = input("Enter new coordinates as floats in format "
                      "'x,y,z': ").strip().replace(" , ", ",").replace(
                        ", ", ",").replace(" ,", ",").split(",")
        if len(n_str) != 3:
            print("Invalid syntax")
            return ()
        return (*xyz_list,) if None not in (xyz_list := [
                try_get_coordinate(str_arg) for str_arg in n_str]) else ()

    while True:
        if set1 := try_get_coordinates():
            return set1


def ft_coordinate_system() -> None:
    def distance(a: tuple[float, float, float],
                 b: tuple[float, float, float]) -> float:
        return sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 + (
                     b[2] - a[2]) ** 2)

    print("Get a first set of coordinates")
    x, y, z = (set1 := get_coordinates())
    print(f"Got a first tuple: {set1}")
    print(f"It includes: X={x:.1f}, Y={y:.1f}, Z={z:.1f}")
    print(f"Distance to center: {distance((0.0, 0.0, 0.0), set1):.4f}")

    print("\nGet a second set of coordinates")
    set2 = get_coordinates()
    print(f"Distance between the 2 sets of coordinates: "
          f"{distance(set1, set2):.4f}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    ft_coordinate_system()
