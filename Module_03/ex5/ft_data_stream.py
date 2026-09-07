import random as r
import typing as t


def gen_event() -> t.Generator[tuple[str, str], None, None]:
    player = ['charlie', 'dylan', 'alice', 'bob']
    action = ['move', 'grab', 'use', 'swim', 'run',
              'climb', 'release', 'eat', 'sleep']
    while True:
        yield (r.choice(player), r.choice(action))


def consume_event(list_tuple: list[tuple[str, str]]
                  ) -> t.Generator[tuple[str, str], None, None]:
    while list_tuple:
        idx = r.randint(0, len(list_tuple) - 1)
        result = list_tuple[idx]
        list_tuple[idx:idx + 1] = []
        # list_tuple[idx:] = list_tuple[idx + 1:]
        yield result


def play_data_stream() -> None:
    event_stream = gen_event()
    for i in range(1000):
        name, action = next(event_stream)
        print(f"Event {i}: Player {name} did action {action}")

    event_stream = gen_event()
    print(f"Built list of 10 events: "
          f"{(list_tuple := [next(event_stream) for _ in range(10)])}")

    for result in consume_event(list_tuple):
        print(f"Got event from list: {result}")
        print(f"Remains in list: {list_tuple}")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    play_data_stream()
