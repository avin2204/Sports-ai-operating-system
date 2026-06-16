from collections import Counter


class PlayerPerformanceAnalyzer:

    def analyze(self, chunks):

        player_stats = Counter()

        players = [

            "virat kohli",
            "rohit sharma",
            "ms dhoni",

            "messi",
            "ronaldo",
            "mbappe",
            "haaland",
            "salah"
        ]

        for chunk in chunks:

            text = chunk.lower()

            for player in players:

                if player in text:

                    player_stats[player] += 1

        return dict(player_stats)