def ft_harvest_total() -> None:
    tot = [0]
    print(f"Total harvest: " + str(
        [tot := [tot[0] + x] for x in [
        int(input(f'Day {i} harvest: ')) for i in [1, 2, 3]]] and tot[0]))
