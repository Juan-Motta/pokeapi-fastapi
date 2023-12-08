from typing import List, Optional

from pydantic import BaseModel


class Pokemon(BaseModel):
    name: str
    url: str


class PokemonResponse(BaseModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[Pokemon]
