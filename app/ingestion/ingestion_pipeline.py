from app.ingestion.pdf_loader import (
    PDFLoaderService
)

from app.ingestion.metadata_extractor import (
    MetadataExtractor
)

from app.rag.chunkers.recursive_chunker import (
    RecursiveChunker
)


class IngestionPipeline:

    def process(
        self,
        pdf_path
    ):

        loader = PDFLoaderService()

        documents = loader.load(
            pdf_path
        )

        chunker = (
            RecursiveChunker()
        )

        extractor = (
            MetadataExtractor()
        )

        all_chunks = []

        for doc in documents:

            metadata = (
                extractor.extract(
                    doc.page_content
                )
            )

            chunks = chunker.chunk(
                doc.page_content
            )

            for chunk in chunks:

                all_chunks.append({

                    "text":
                        chunk,

                    "metadata":
                        metadata
                })

        return all_chunks