from pathlib import Path

from app.ingestion.parsers.pdf_parser import (
    PDFParser
)

from app.ingestion.parsers.docx_parser import (
    DOCXParser
)

from app.ingestion.parsers.text_parser import (
    TextParser
)

from app.ingestion.parsers.csv_parser import (
    CSVParser
)

from app.ingestion.parsers.pptx_parser import (
    PPTXParser
)

from app.ingestion.parsers.image_parser import (
    ImageParser
)


class ParserFactory:

    @staticmethod
    def get_parser(
        file_path: str
    ):

        suffix = (
            Path(file_path)
            .suffix
            .lower()
        )

        mapping = {

            ".pdf":
            PDFParser(),

            ".docx":
            DOCXParser(),

            ".txt":
            TextParser(),

            ".csv":
            CSVParser(),

            ".pptx":
            PPTXParser(),

            ".png":
            ImageParser(),

            ".jpg":
            ImageParser(),

            ".jpeg":
            ImageParser()
        }

        if suffix not in mapping:

            raise ValueError(
                f"Unsupported file: {suffix}"
            )

        return mapping[suffix]