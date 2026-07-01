import pytesseract

from PIL import Image

from app.ingestion.models.document import (
    Document
)

from app.ingestion.parsers.base_parser import (
    BaseParser
)


class ImageParser(BaseParser):

    def parse(
        self,
        file_path: str
    ) -> Document:

        image = Image.open(
            file_path
        )

        text = pytesseract.image_to_string(
            image
        )

        return Document(
            content=text,
            metadata={},
            source=file_path,
            document_type="image"
        )