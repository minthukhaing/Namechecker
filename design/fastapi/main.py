
# import sys
# from pathlib import Path

# # လက်ရှိ working directory ကို add လုပ်ပေးသည်
# sys.path.append(str(Path(__file__).parent.parent))
# from models.my_en_convert import myan
# from models.pali_my_convert import parli



from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

#call model
from models.my_en_convert import myan
from models.pali_my_convert import parli
import asyncio

# Secret key နဲ့ algorithm
SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# FastAPI instance
app = FastAPI()

# Security setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Sample User Model
class User(BaseModel):
    username: str

# Request model for login
class UserInDB(User):
    hashed_password: str

# Login form အတွက် model
class TokenData(BaseModel):
    username: str | None = None

# Input အတွက် model
class TextInput(BaseModel):
    text: str

# စက်ဝိုင်းဆိုင်ရာ database နဲ့တူတဲ့ dummy data
fake_users_db = {
    "admin": {
        "username": "admin",
        "hashed_password": pwd_context.hash("nc"),
    }
}

# JWT ဖန်တီးဖို့ function
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Dependency အတွက် function
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = fake_users_db.get(token_data.username)
    if user is None:
        raise credentials_exception
    return user

# Token ရယူဖို့ endpoint
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if user_dict is None or not pwd_context.verify(form_data.password, user_dict["hashed_password"]):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user_dict["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Secured POST endpoint
@app.post("/myanmar_to_english")
def myanmar_to_english(input: TextInput, current_user: User = Depends(get_current_user)):
    txt=input.text

    result=asyncio.run(myan(txt))

    return {
        "received_text": result,
        "length": len(input.text),
        "message": f"Thank you for the text(myanmar_to_english): '{input.text}'",
        "user": current_user["username"]
    }

@app.post("/parli_to_roman")
def parli_to_roman(input: TextInput, current_user: User = Depends(get_current_user)):
    txt=input.text

    result=asyncio.run(parli(txt))

    return {
        "received_text": result,
        "length": len(input.text),
        "message": f"Thank you for the text(parli_to_roman): '{input.text}'",
        "user": current_user["username"]
    }