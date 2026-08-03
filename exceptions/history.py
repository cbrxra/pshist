from exceptions.base import TerminalError
from pathlib import Path

class HistoryError(TerminalError):
    pass

class HistoryFileNotFoundError(HistoryError):
    def __init__(self, path: Path):
        super().__init__(f"History file '{path} does not exits.")
        self.path = path

class HistoryWriteError(HistoryError):

    def __init__(self, path: Path):
        super().__init__(f"Could not write history file '{path}'.")
        self.path = path

class HistoryEmptyError(HistoryError):
    def __init__(self):
        super().__init__("The history is empty.")

class HistoryAddCountError(HistoryError):

    def __init__(self, count :int):
        super().__init__(f"Cannot add {count} commands. Count must be greater than 0.")
        self.count = count

class HistoryDeleteIndexError(HistoryError):

    def __init__(self, index :int):
        super().__init__(f"Cannot delete command at index {index}. Index must be greater than or equal to 0.")
        self.index = index

class HistoryDeleteIndexLenError(HistoryError):

    def __init__(self, index :int, len_data :int):
        super().__init__(f"Cannot delete {index} command. index must less than {len_data - 1}.")
        self.index = index
        self.len_data = len_data
