from pydantic import BaseModel
from models.user_model import User

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
