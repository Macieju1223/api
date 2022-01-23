from fastapi import APIRouter, Depends
from database import get_db
import schem,models
from typing import List
from sqlalchemy.orm import Session
from .oauth2 import get_current_user

router = APIRouter(
    tags = ['Rosliny']
)

@router.post('/Rosliny')
def dodawanie_roslin(request: schem.rosliny,db: Session = Depends(get_db),current_user: schem.login = Depends(get_current_user)):
    roslina = models.rosliny(
       nazwa = request.nazwa,
       polka_id = 1
    )
    db.add(roslina)
    db.commit()
    db.refresh(roslina)
    return roslina

@router.get('/Rosliny/{nazwa}')
def dostepne_rosliny_w_magazynie(db: Session = Depends(get_db)):
    rosliny = db.query(models.rosliny).all()
    return rosliny

@router.get('/Rosliny/{id_rosliny}',response_model=schem.roslina_id)
def szukana_roslinka_podaj_id(id_rosliny,db: Session = Depends(get_db)):
    szukana = db.query(models.rosliny).filter(models.rosliny.id_rosliny == id_rosliny).first()
    return szukana