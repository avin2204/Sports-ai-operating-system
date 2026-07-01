from pydantic import BaseModel


class DocumentFilterResponse(
    BaseModel
):

    id: int

    filename: str

    file_type: str