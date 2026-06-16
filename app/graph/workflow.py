from app.agents.player_agent import player_agent
from app.agents.team_agent import team_agent
from app.agents.statistics_agent import statistics_agent
from app.agents.prediction_agent import prediction_agent

from app.agents.injury_agent import injury_agent

from app.agents.transfer_agent import transfer_agent

from app.agents.commentary_agent import commentary_agent

from app.agents.scouting_agent import scouting_agent

from app.agents.fantasy_team_agent import fantasy_team_agent

from app.agents.match_prediction_agent import (
    match_prediction_agent
)


builder.add_node(
    "player",
    player_agent
)

builder.add_node(
    "team",
    team_agent
)

builder.add_node(
    "statistics",
    statistics_agent
)

builder.add_node(
    "prediction",
    prediction_agent
)

builder.add_edge(
    "retrieval",
    "player"
)

builder.add_edge(
    "player",
    "team"
)

builder.add_edge(
    "team",
    "statistics"
)

builder.add_edge(
    "statistics",
    "prediction"
)

builder.add_node(
    "injury",
    injury_agent
)

builder.add_node(
    "transfer",
    transfer_agent
)

builder.add_node(
    "scouting",
    scouting_agent
)

builder.add_node(
    "commentary",
    commentary_agent
)


builder.add_edge(
    "statistics",
    "injury"
)

builder.add_edge(
    "injury",
    "transfer"
)

builder.add_edge(
    "transfer",
    "scouting"
)

builder.add_edge(
    "scouting",
    "commentary"
)

builder.add_edge(
    "commentary",
    "prediction"
)

builder.add_node(
    "fantasy_team",
    fantasy_team_agent
)

builder.add_node(
    "match_prediction",
    match_prediction_agent
)

builder.add_edge(
    "prediction",
    "fantasy_team"
)

builder.add_edge(
    "fantasy_team",
    "match_prediction"
)