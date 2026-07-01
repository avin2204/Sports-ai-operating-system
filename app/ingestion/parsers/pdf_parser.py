import fitz

from app.ingestion.models.document import (
    Document
)

from app.ingestion.parsers.base_parser import (
    BaseParser
)


class PDFParser(BaseParser):

    def parse(
        self,
        file_path: str
    ) -> Document:

        doc = fitz.open(file_path)

        text = ""

        for page in doc:
            text += page.get_text()

        return Document(
            content=text,
            metadata={
                "pages": len(doc)
            },
            source=file_path,
            document_type="pdf"
        )