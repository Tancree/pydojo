from pydantic import BaseModel


class Game(BaseModel):
    name: str
    id: str

    def __repr__(self) -> str:
        return (f"Game: {self.name} [ID: {self.id}]")
