from pydantic import BaseModel


class DocumentSearchResponse(
    BaseModel
):

    id: int

    filename: str

    file_type: str
    