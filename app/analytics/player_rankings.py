from collections import Counter


class PlayerRankings:

    def rank(self, chunks):

        counter = Counter()

        players = [

            "virat kohli",
            "rohit sharma",
            "ms dhoni",

            "messi",
            "ronaldo",
            "haaland",
            "mbappe",
            "salah"
        ]

        for chunk in chunks:

            text = chunk.lower()

            for player in players:

                if player in text:

                    counter[player] += 1

        return counter.most_common()