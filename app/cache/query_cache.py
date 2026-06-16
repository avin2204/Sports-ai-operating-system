import hashlib


class QueryCache:

    def key(
        self,
        query
    ):

        return hashlib.md5(
            query.encode()
        ).hexdigest()