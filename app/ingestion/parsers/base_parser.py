from abc import ABC
from abc import abstractmethod

from app.ingestion.models.document import (
    Document
)


class BaseParser(ABC):

    @abstractmethod
    def parse(
        self,
        file_path: str
    ) -> Document:
        pass