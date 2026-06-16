from collections import Counter


class TeamComparison:

    def compare(self, chunks):

        team_counter = Counter()

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

                    team_counter[team] += 1

        return dict(team_counter)