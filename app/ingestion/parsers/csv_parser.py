import pandas as pd

from app.ingestion.models.document import (
    Document
)

from app.ingestion.parsers.base_parser import (
    BaseParser
)


class CSVParser(BaseParser):

    def parse(
        self,
        file_path: str
    ) -> Document:

        df = pd.read_csv(
            file_path
        )

        text = df.to_string()

        return Document(
            content=text,
            metadata={
                "rows": len(df)
            },
            source=file_path,
            document_type="csv"
        )