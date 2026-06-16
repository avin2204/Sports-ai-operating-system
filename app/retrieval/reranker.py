class Reranker:

    def rerank(
        self,
        docs
    ):

        ranked = sorted(

            docs,

            key=lambda x:
            x.get(
                "score",
                0
            ),

            reverse=True
        )

        return ranked[:10]
    