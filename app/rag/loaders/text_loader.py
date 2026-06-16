from app.rag.loaders.base_loader import BaseLoader


class TextLoader(BaseLoader):

    def load(self, file_path: str) -> str:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()