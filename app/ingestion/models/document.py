from dataclasses import dataclass
from typing import Dict


@dataclass
class Document:

    content: str

    metadata: Dict

    source: str

    document_type: str