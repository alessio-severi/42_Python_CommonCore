import random as r


def ft_data() -> None:
    data = ['Alice', 'bob', 'Liam', 'Charlie', 'dylan',
            'Emma', 'Gregory', 'john', 'kevin']
    print(f"Initial list of players: {data}")
    list1 = [x.capitalize() for x in data]
    print(f"New list with all names capitalized: {list1}")
    list2 = [x for x in data if x == x.capitalize()]
    print(f"New list of capitalized names only: {list2}\n")
    score_dict = {x: r.randint(1, 999) for x in list1}
    print(f"Score dict: {score_dict}")
    average = sum(score_dict[x] for x in score_dict) / len(score_dict)
    print(f"Score average is {average:.2f}")
    high_s = {x: score_dict[x] for x in score_dict if score_dict[x] > average}
    print(f"High scores: {high_s}")


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    ft_data()
