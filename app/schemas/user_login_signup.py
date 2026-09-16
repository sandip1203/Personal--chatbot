from pydantic import BaseModel 


class Login(BaseModel):
    email:str
    password:str
    
class Register(BaseModel):
    name :str
    email:str
    location:str
    gender :str
    password :str