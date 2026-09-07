from abc import ABC
from abc import abstractmethod
from typing import Any


class DataProcessor(ABC):
    _data_storage: list[str]

    def __init__(self) -> None:
        self._data_storage = []
        self._count = -1

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if len(self._data_storage) < 1:
            raise ValueError(f"Alert: The data memory is {tuple()}.")
        self._count += 1
        return (self._count, self._data_storage.pop(0))


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        return (isinstance(data, list) and
                all(map(lambda x: isinstance(x, (int, float)), data))
                or isinstance(data, (int, float)))

    def ingest(self, data: list[int | float] | int | float) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        flag = False
        if isinstance(data, int | float):
            data = [data]
            flag = True
        print((f" Processing data: {data[0]}") if flag
              else f" Processing data: {data}")
        (self._data_storage.extend(
         map(lambda x: str(x) if isinstance(x, int)
             else f"{x:.1f}", data)))


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        return (isinstance(data, list) and
                all(map(lambda x: isinstance(x, str), data))
                or isinstance(data, str))

    def ingest(self, data: list[str] | str) -> None:
        if not self.validate(data):
            raise ValueError("Improper string data")

        print(f" Processing data: {data}")
        (self._data_storage.extend(data) if isinstance(data, list)
            else self._data_storage.append(data))


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        def is_keysstr_and_valuesstr(item: Any) -> bool:
            return (isinstance(item, dict) and
                    all(map(lambda x: isinstance(x[0], str)
                        and isinstance(x[1], str), item.items())))

        return (isinstance(data, list)
                and all(map(lambda x: is_keysstr_and_valuesstr(x), data))
                or is_keysstr_and_valuesstr(data))

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        def add_dict(item: dict[str, str]) -> None:
            if (len(item) == 2
                    and list(item.keys()) == ['log_level', 'log_message']):
                self._data_storage.append(
                    f"{item['log_level']}: {item['log_message']}")
            else:
                temp = list(map(lambda x: f"{x[0]}: {x[1]}", item.items()))
                self._data_storage.append(", ".join(temp))

        if not self.validate(data):
            raise ValueError("Improper log data")

        print(f" Processing data: {data}")
        if isinstance(data, dict):
            data = [data]
        for x in data:
            add_dict(x)


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")

    d = NumericProcessor()
    for x in (42, "Hello"):
        print(f" Trying to validate input \'{x}\': {d.validate(x)}")
    # test invalid
    input1 = "foo"
    print(f" Test invalid ingestion of string "
          f"\'{input1}\' without prior validation:")
    try:
        d.ingest(input1)
    except ValueError as error:
        print(f" Got exception: {error}")
    # test valid
    d.ingest([1, 2, 3, 4, 5])
    # test valid
    n = 3
    print(f" Extracting {n} values...")
    for _ in range(n):
        (val := d.output()) and print(f" Numeric value {val[0]}: {val[1]}")

    print("\nTesting Text Processor...")

    t = TextProcessor()
    for x in ("Hello", 42):
        print(f" Trying to validate input \'{x}\': {t.validate(x)}")
    # test invalid
    y = [42, "Hello"]
    print(f" Test invalid ingestion of list \'{y}\' without prior validation:")
    try:
        t.ingest(y)
    except ValueError as error:
        print(f" Got exception: {error}")
    # test valid
    t.ingest(['Hello', 'Nexus', 'World'])
    # test valid
    n = 1
    print(f" Extracting {n} value...")
    (val := t.output()) and print(f" Text value {val[0]}: {val[1]}")

    print("\nTesting Log Processor...")

    log = LogProcessor()
    log_test = [
        [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
         {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}], 42]
    for x1 in log_test:
        print(f" Trying to validate input \'{x1}\': {log.validate(x1)}")
    # test invalid
    print(f" Test invalid ingestion of list \'{y}\' without prior validation:")
    try:
        log.ingest(y)
    except ValueError as error:
        print(f" Got exception: {error}")
    # test valid
    log.ingest(
        [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
         {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}])
    # test valid
    n = 2
    print(f" Extracting {n} values...")
    for _ in range(n):
        (val := log.output()) and print(f" Log entry {val[0]}: {val[1]}")
