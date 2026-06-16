from abc import ABC, abstractmethod


class BaseVectorStore(ABC):

    @abstractmethod
    def add(
        self,
        text: str,
        embedding: list[float]
    ):
        pass

    @abstractmethod
    def search(
        self,
        embedding: list[float],
        top_k: int = 3
    ):
        pass