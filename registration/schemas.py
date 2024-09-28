from pydantic import BaseModel

class Usercreate(BaseModel):
    username: str
    email:str
    position:str
    


class ShowUserSchema(BaseModel):
    id: str
    username:str
    email:str
    

    class Config:
        orm_mode = True



