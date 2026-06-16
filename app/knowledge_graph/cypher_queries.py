GET_PLAYER_TEAMS = """
MATCH (p:Player)-[:PLAYS_FOR]->(t)
WHERE p.name = $player
RETURN t.name
"""