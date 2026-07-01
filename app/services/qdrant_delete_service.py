from qdrant_client import (
    QdrantClient
)


class QdrantDeleteService:

    def __init__(self):

        self.client = (
            QdrantClient(
                host="localhost",
                port=6333
            )
        )

        self.collection = (
            "sports_docs"
        )

    def delete_point(
        self,
        point_id
    ):

        self.client.delete(

            collection_name=
            self.collection,

            points_selector=[
                point_id
            ]
        )