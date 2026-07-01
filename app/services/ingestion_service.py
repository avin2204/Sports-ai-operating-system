from app.services.document_service import (
    DocumentService
)

from app.services.chunking_service import (
    ChunkingService
)

from app.services.embedding_service import (
    EmbeddingService
)

from app.services.qdrant_ingestion_service import (
    QdrantIngestionService
)


class IngestionService:

    def __init__(self):

        self.document_service = (
            DocumentService()
        )

        self.chunking_service = (
            ChunkingService()
        )

        self.embedding_service = (
            EmbeddingService()
        )

        self.qdrant_service = (
            QdrantIngestionService()
        )

    def ingest(
        self,
        file_path: str
    ):

        document = (
            self.document_service.process(
                file_path
            )
        )

        print(
            "\n========== DOCUMENT DEBUG =========="
        )

        print(
            f"FILE: {file_path}"
        )

        print(
            f"CONTENT LENGTH: {len(document.content)}"
        )

        print(
            f"METADATA: {document.metadata}"
        )

        print(
            "\nFIRST 500 CHARS:\n"
        )

        print(
            document.content[:500]
        )

        chunks = (
            self.chunking_service.chunk(
                document.content
            )
        )

        print(
            f"\nTOTAL CHUNKS: {len(chunks)}"
        )

        if len(chunks) > 0:

            print(
                "\nFIRST CHUNK:\n"
            )

            print(
                chunks[0][:500]
            )

        print(
            "\n====================================\n"
        )

        stored_chunks = 0

        for chunk in chunks:

            embedding = (
                self.embedding_service.embed(
                    chunk
                )
            )

            self.qdrant_service.store_chunk(

                chunk=chunk,

                embedding=embedding
            )

            stored_chunks += 1

        return {

            "status":
            "success",

            "file":
            document.source,

            "chunks":
            stored_chunks
        }