
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserIn(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: str | None = None


def fake_password_hasher(raw_password: str):
    return "yubrajupdahaya" + raw_password

def fake_save_user(user_in: UserIn):
    hashed_paasword = fake_password_hasher(user_in.password)
    user_in_db = UserDB(**user_in.dict(), hashed_password=hashed_paasword)
    return user_in_db

@app.post('/user', response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved


# Reduce Duplication 

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str


class ReduceUserIn(UserBase):
    password: str

class ReduceUserOut(UserBase):
    pass

class UserInDB(UserBase):
    hashed_password: str

