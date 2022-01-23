from fastapi import APIRouter, Depends
from database import get_db
import schem,models
from typing import List
from sqlalchemy.orm import Session
from . import encryption
from .oauth2 import get_current_user

router = APIRouter(
    tags = ['Urzytkownicy']
)

@router.get('/User',response_model=List[schem.urzytkownicy])
def wyswietl_urzytkownikow(db: Session = Depends(get_db),current_user: schem.login = Depends(get_current_user)):
    urzytkownicy = db.query(models.user).all()
    return urzytkownicy

@router.post('/User')
def dodaj_urzytkownika(request: schem.login,db: Session = Depends(get_db),current_user: schem.login = Depends(get_current_user)):
    new_user = models.user(
        username = request.username,
        password = encryption.hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.delete('/User/{username}')
def usuwa_urzytkownika(username, db: Session = Depends(get_db)):
    db.query(models.user).filter(models.user.username == username).delete(synchronize_session=False)
    db.commit()
    return 'done'

@router.put('/User/{id}')
def edycja_hasla_urzytkownika(id,request: schem.login,db: Session = Depends(get_db),current_user: schem.login = Depends(get_current_user)):
    db.query(models.user).filter(models.user.id == id).update({
        'username': request.username,
        'password': request.password
    })
    db.commit()
    return 'done'
