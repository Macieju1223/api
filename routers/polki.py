from fastapi import APIRouter, Depends
from database import get_db
import schem,models
from typing import List
from sqlalchemy.orm import Session
from .oauth2 import get_current_user
router = APIRouter(
    tags = ['Polki']
)

@router.post('/Polki')
def dodawanie_polek_so_sektorow(request: schem.polka,db: Session = Depends(get_db),current_user: schem.login = Depends(get_current_user)):
    polka = models.polki(
       sektor = request.sektor 
    )
    db.add(polka)
    db.commit()
    db.refresh(polka)
    return polka

@router.get('/Polki')
def wyswietl_sektory(db: Session = Depends(get_db)):
    sektory = db.query(models.polki).all()
    return sektory

@router.get('/Polki/{id_polki}')
def wyswietl_sektor_w_ktorym_najduje_sie_polka(id,db: Session = Depends(get_db)):
    sektory = db.query(models.polki).filter(models.polki.id_polki == id).first()
    return sektory