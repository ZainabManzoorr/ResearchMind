from pathlib import Path


class DocumentLoader:

    def load(self, path: str):

        return Path(path).read_text(
            encoding="utf-8"
        )