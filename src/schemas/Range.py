from pydantic import BaseModel

class Range(BaseModel):
     type_report:str
     start_date:str
     end_date:str