from abc import ABC
from abc import abstractmethod


class BaseMemory(ABC):

    @abstractmethod
    def save(
        self,
        session_id: str,
        role: str,
        content: str
    ):
        pass

    @abstractmethod
    def get_history(
        self,
        session_id: str
    ):
        pass