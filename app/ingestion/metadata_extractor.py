import os


class MetadataExtractor:

    @staticmethod
    def extract(
        file_path: str
    ):

        stat = os.stat(
            file_path
        )

        return {

            "file_name":
            os.path.basename(
                file_path
            ),

            "size":
            stat.st_size
        }