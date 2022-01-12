from fastapi import APIRouter, Depends
from database import get_db
import schem,models
from typing import List
from sqlalchemy.orm import Session

router = APIRouter(
    tags = ['Urzytkownicy']
)

@router.get('/User',response_model=List[schem.urzytkownicy])
def wyswietl_urzytkownikow(db: Session = Depends(get_db)):
    firmy = db.query(models.user).all()
    return firmy

@router.post('/User')
def dodaj_urzytkownika(request: schem.login,db: Session = Depends(get_db)):
    new_user = models.user(
        login = request.login,
        haslo = request.haslo
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.delete('/User/{login}')
def usuwa_urzytkownika(login, db: Session = Depends(get_db)):
    db.query(models.user).filter(models.user.login==login).delete(synchronize_session=False)
    db.commit()
    return 'done'

@router.put('/User/{id}{login}{haslo}')
def edycja_hasla_urzytkownika(login,haslo,request: schem.login,db: Session = Depends(get_db)):
    db.query(models.user).filter(models.user.login == login,models.user.haslo == haslo).update({
        'login': request.login,
        'haslo': request.haslo
    })
    db.commit()
    return 'done'
