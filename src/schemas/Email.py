from pydantic import BaseModel
class EmailItem(BaseModel):
    subject: str
    message: str
    to_email: str

