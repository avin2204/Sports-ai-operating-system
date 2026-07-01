import json

from kafka import KafkaProducer


class KafkaEventProducer:

    def __init__(self):

        self.producer = KafkaProducer(

            bootstrap_servers=
            "localhost:9092",

            value_serializer=lambda v:
            json.dumps(v).encode(
                "utf-8"
            )
        )

    def publish(
        self,
        topic: str,
        payload: dict
    ):

        self.producer.send(
            topic,
            payload
        )

        self.producer.flush()