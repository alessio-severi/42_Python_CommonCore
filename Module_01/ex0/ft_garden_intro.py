##!/usr/bin/env python3
"""
Usage:
1. Remove "#" from line 1.

2. Run in your terminal:
        chmod u+x ft_garden_intro.py
        ./ft_garden_intro.py
"""


def ft_garden_intro() -> None:
    plant = "Rose"
    height = "25"
    age = "30"

    print(f"=== Welcome to My Garden ===\n"
          f"Plant: {plant}\n"
          f"Height: {height}cm\n"
          f"Age: {age} days\n\n"
          f"=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
