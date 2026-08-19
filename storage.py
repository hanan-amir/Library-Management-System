import json
from pathlib import Path


class JSONStorage:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        if not self.file_path.exists():
            self._write([])

    def _write(self, data: list):
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def read(self) -> list:
        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                return json.load(file)

        except json.JSONDecodeError:
            return []

    def write(self, data: list):
        self._write(data)