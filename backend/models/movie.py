from typing import Optional
from pydantic import BaseModel

class movies(BaseModel):
    idM: Optional[str]
    src: str
    genero: str
    clasif: str
    year: str
    duracion: str
    comments: str
