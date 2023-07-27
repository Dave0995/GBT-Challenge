from pydantic import BaseModel

class Deparments(BaseModel):
    id: int
    department: str

    
class HiredEmployees(BaseModel):
    id: int
    name: str
    datetime: str
    department_id: int
    job_id: int
    

class Jobs(BaseModel):
    id: int
    job: str
