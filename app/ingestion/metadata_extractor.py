class MetadataExtractor:

    def extract(
        self,
        text
    ):

        metadata = {

            "sport": None,

            "team": None,

            "player": None,

            "season": None
        }

        lower = text.lower()

        if "ipl" in lower:

            metadata["sport"] = (
                "cricket"
            )

        if "epl" in lower:

            metadata["sport"] = (
                "football"
            )

        if "virat kohli" in lower:

            metadata["player"] = (
                "Virat Kohli"
            )

        if "messi" in lower:

            metadata["player"] = (
                "Messi"
            )

        return metadata