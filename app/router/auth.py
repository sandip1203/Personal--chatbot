from fastapi import APIRouter, Depends
from app.db.database import get_db
from app.models.user_models import User
from app.schemas.user_login_signup import Register
from sqlalchemy.orm import Session

auth_router = APIRouter()


@auth_router.get("/")
def home():
    return {"message":"this is home page of personal chatbot"}

@auth_router.post("/users")
def create_user(
    user:Register,
    db:Session = Depends(get_db)
):
    new_user = User(
        name =user.name,
        email = user.email,
        location = user.location,
        gender = user.gender ,
        password = user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user