from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
import models,database
from sqlalchemy.orm import Session
from . import encryption,jwt_token

router = APIRouter(
    tags= ['Autentication']
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(),db: Session = Depends(database.get_db)):
    user = db.query(models.user).filter(models.user.username == request.username).first()
    if not user:
        return 'nope, no user wit that name'
    if not encryption.hash.verify(user.password,request.password):
        return 'incorect password'
    # generate jwt token
    access_token = jwt_token.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}