from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str]
    name: str
    Lname: str
    username: str
    email: str
    password: str
