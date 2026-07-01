from app.ingestion.parser_factory import (
    ParserFactory
)

from app.ingestion.metadata_extractor import (
    MetadataExtractor
)


class DocumentService:

    def process(
        self,
        file_path: str
    ):

        parser = (
            ParserFactory.get_parser(
                file_path
            )
        )

        document = parser.parse(
            file_path
        )

        document.metadata.update(

            MetadataExtractor.extract(
                file_path
            )

        )

        return document