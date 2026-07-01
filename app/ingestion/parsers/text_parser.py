from app.ingestion.models.document import (
    Document
)

from app.ingestion.parsers.base_parser import (
    BaseParser
)


class TextParser(BaseParser):

    def parse(
        self,
        file_path: str
    ) -> Document:

        with open(
            file_path,
            encoding="utf-8"
        ) as f:

            text = f.read()

        return Document(
            content=text,
            metadata={},
            source=file_path,
            document_type="txt"
        )