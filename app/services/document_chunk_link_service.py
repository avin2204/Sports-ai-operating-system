from app.services.document_metadata_service import (
    DocumentMetadataService
)


class DocumentChunkLinkService:

    def __init__(self):

        self.metadata_service = (
            DocumentMetadataService()
        )

    def build_payload(

        self,

        file_path: str,

        document_id: int,

        chunk: str
    ):

        metadata = (

            self.metadata_service.build_metadata(
                file_path
            )
        )

        return {

            "document_id":
            document_id,

            "filename":
            metadata["filename"],

            "file_type":
            metadata["file_type"],

            "text":
            chunk
        }
    