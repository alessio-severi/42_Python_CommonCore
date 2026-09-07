from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import Protocol


class ExportPlugin(Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVPlugin:

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        if not data:
            print()
        else:
            print(",".join(list(map(lambda x: f'{x[1] if x else ""}', data))))


class JSONPlugin:

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        if not data:
            print("{}")
        elif not (tuple() in data):
            print("{" + ", ".join(
                list(("\"item_" + str(x) + "\": " + "\"" + y + "\"" for x, y
                      in data))) + "}")
        else:
            raise ValueError("Error: invalid data list")


class DataProcessor(ABC):
    _data_storage: list[str]

    def __init__(self) -> None:
        self._data_storage = []
        self._count = -1
        self._count_total_ingest = 0
        self._count_total_remaining = 0

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
        self._count_total_remaining -= 1
        return (self._count, self._data_storage.pop(0))

    @property
    def count_total_ingest(self) -> int:
        return self._count_total_ingest

    @property
    def count_total_remaining(self) -> int:
        return self._count_total_remaining


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        return (isinstance(data, list) and
                all(map(lambda x: isinstance(x, (int, float)), data))
                or isinstance(data, (int, float)))

    def ingest(self, data: list[int | float] | int | float) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        temp = len(self._data_storage)
        # flag = False
        if isinstance(data, int | float):
            data = [data]
        #    flag = True
        # print((f" Processing data: {data[0]}") if flag
        #      else f" Processing data: {data}")
        (self._data_storage.extend(
            (list(map(lambda x: str(x) if isinstance(x, int)
                      else f"{x:.2f}", data)))))
        self._count_total_ingest += len(self._data_storage) - temp
        self._count_total_remaining += len(self._data_storage) - temp


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        return (isinstance(data, list) and
                all(map(lambda x: isinstance(x, str), data))
                or isinstance(data, str))

    def ingest(self, data: list[str] | str) -> None:
        if not self.validate(data):
            raise ValueError("Improper string data")

        temp = len(self._data_storage)
        # print(f" Processing data: {data}")
        (self._data_storage.extend(data) if isinstance(data, list)
            else self._data_storage.append(data))
        self._count_total_ingest += len(self._data_storage) - temp
        self._count_total_remaining += len(self._data_storage) - temp


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

        temp = len(self._data_storage)
        # print(f" Processing data: {data}")
        if isinstance(data, dict):
            data = [data]
        for x in data:
            add_dict(x)
        self._count_total_ingest += len(self._data_storage) - temp
        self._count_total_remaining += len(self._data_storage) - temp


class DataStream:
    __data_processor: list[DataProcessor]

    def __init__(self) -> None:
        print("Initialize Data Stream...")
        self.__data_processor = []

    def register_processor(self, proc: DataProcessor) -> None:
        if any(map(lambda x: type(proc) is type(x), self.__data_processor)):
            return print(f"{type(proc).__name__.replace(
                "Processor", " Processor")} already registered")
        self.__data_processor.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for y in stream:
            objs: list[DataProcessor]
            if not (objs := list(filter(lambda x: x.validate(y),
                                        self.__data_processor))):
                print(f"DataStream error - Can't process element in stream: "
                      f"{y}")
            else:
                objs[0].ingest(y)

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
        if not self.__data_processor:
            return print("No processor found, no data\n")

        for x in self.__data_processor:
            name_with_sp = type(x).__name__.replace("Processor", " Processor")
            print(f"{name_with_sp}: total {x.count_total_ingest} items process"
                  f"ed, remaining {x.count_total_remaining} on processor")
        return print()

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        print(f"Send {nb} processed data from each processor to a "
              f"{plugin.__class__.__name__.replace('Plugin', ' plugin')}:")
        for x in self.__data_processor:
            idx_min = min(nb, x.count_total_remaining)
            items = [x.output() for _ in range(idx_min)]
            plugin.process_output(items)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")

    s = DataStream()
    s.print_processors_stats()

    print("Registering Processor\n")
    d = NumericProcessor()
    s.register_processor(d)
    t = TextProcessor()
    s.register_processor(t)
    log = LogProcessor()
    s.register_processor(log)

    input1 = ['Hello world', [3.14, -1, 2.71],
              [{'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'},
               {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
              42, ['Hi', 'five']]
    print(f"Send first batch of data on stream: {input1}")
    s.process_stream(input1)
    s.print_processors_stats()

    s.output_pipeline(3, CSVPlugin())
    s.print_processors_stats()

    input1 = [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
              [{'log_level': 'ERROR', 'log_message': '500 server crash'},
               {'log_level': 'NOTICE', 'log_message': 'Certificate expires in '
               '10 days'}], [32, 42, 64, 84, 128, 168], 'World hello']
    print(f"Send another batch of data: {input1}")
    s.process_stream(input1)
    s.print_processors_stats()

    s.output_pipeline(5, JSONPlugin())
    s.print_processors_stats()
