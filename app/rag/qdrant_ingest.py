from qdrant_client import (
    QdrantClient
)

from qdrant_client.models import (
    PointStruct
)


class QdrantIngest:

    def __init__(self):

        self.client = (
            QdrantClient(
                host="localhost",
                port=6333
            )
        )

    def store(

        self,

        collection_name,

        vectors

    ):

        points = []

        for idx, item in enumerate(
            vectors
        ):

            points.append(

                PointStruct(

                    id=idx,

                    vector=item[
                        "vector"
                    ],

                    payload=item
                )
            )

        self.client.upsert(

            collection_name=
            collection_name,

            points=points
        )