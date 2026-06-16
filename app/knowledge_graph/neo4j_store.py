from neo4j import GraphDatabase


class Neo4jStore:

    def __init__(

        self,

        uri,

        username,

        password

    ):

        self.driver = (
            GraphDatabase.driver(
                uri,
                auth=(
                    username,
                    password
                )
            )
        )

    def create_player(

        self,

        player

    ):

        query = """
        CREATE (p:Player {
            name:$name
        })
        """

        with self.driver.session() as s:

            s.run(
                query,
                name=player
            )
            