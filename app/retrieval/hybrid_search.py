from rank_bm25 import BM25Okapi


class HybridSearch:

    def keyword_search(
        self,
        query,
        documents
    ):

        tokenized_docs = [
            doc.split()
            for doc in documents
        ]

        bm25 = BM25Okapi(
            tokenized_docs
        )

        scores = bm25.get_scores(
            query.split()
        )

        return scores