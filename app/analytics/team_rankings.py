from collections import Counter


class TeamRankings:

    def rank(self, chunks):

        counter = Counter()

        teams = [

            "india",
            "australia",
            "england",

            "rcb",
            "csk",
            "mi",

            "arsenal",
            "liverpool",
            "barcelona",
            "real madrid"
        ]

        for chunk in chunks:

            text = chunk.lower()

            for team in teams:

                if team in text:

                    counter[team] += 1

        return counter.most_common()