from pydantic import BaseModel


class DocumentRequest(
    BaseModel
):

    filename: str