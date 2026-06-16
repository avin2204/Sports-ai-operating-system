class PredictionAccuracy:

    def evaluate(
        self,
        predictions,
        actuals
    ):

        total = len(predictions)

        if total == 0:
            return 0

        correct = 0

        for pred, actual in zip(
            predictions,
            actuals
        ):

            if pred == actual:

                correct += 1

        return round(
            (
                correct / total
            ) * 100,
            2
        )