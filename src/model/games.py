from pydantic import BaseModel


class Games(BaseModel):
    name: str
    id: str
