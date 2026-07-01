import os


class DocumentMetadataService:

    def build_metadata(
        self,
        file_path: str
    ):

        return {

            "filename":
            os.path.basename(
                file_path
            ),

            "file_type":
            file_path.split(".")[-1]
        }