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

class HistoryAddCountError(HistoryError):

    def __init__(self, count :int):
        super().__init__(f"Cannot add {count} commands. Count must be greater than 0.")
        self.count = count