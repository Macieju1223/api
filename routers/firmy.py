from fastapi import APIRouter, Depends
from database import get_db
import schem,models
from typing import List
from sqlalchemy.orm import Session
from .oauth2 import get_current_user

router = APIRouter(
    tags = ['Firmy']
)

@router.get('/Firmy',response_model=List[schem.podstawowe_informacje])
def wyswietl_firmy(db: Session = Depends(get_db),current_user: schem.login = Depends(get_current_user)):
    firmy = db.query(models.firma).all()
    return firmy

@router.post('/Firmy')
def dodaj_firme(request: schem.firma,db: Session = Depends(get_db),current_user: schem.login = Depends(get_current_user)):
    new_company = models.firma(
        nazwa = request.nazwa,
        miasto = request.miasto,
        ulica = request.ulica,
        numer = request.numer,
        kod_pocztowy = request.kod_pocztowy,
        numer_telefonu = request.numer_telefonu
    )
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company

@router.get('/Firmy/{numer}')
def wyswietl_firme_poprzez_podanie_numeru(numer,db: Session = Depends(get_db),current_user: schem.login = Depends(get_current_user)):
    firma = db.query(models.firma).filter(models.firma.numer == numer).first()
    return firma

@router.delete('/Firma/{id}')
def usuwa_firme_z_bazy(id, db: Session = Depends(get_db),current_user: schem.login = Depends(get_current_user)):
    db.query(models.firma).filter(models.firma.id==id).delete(synchronize_session=False)
    db.commit()
    return 'done'

@router.put('/Firma/{id}',)
def edycja_informacji_dotyczacych_firmy(id,request: schem.firma,db: Session = Depends(get_db),current_user: schem.login = Depends(get_current_user)):
    db.query(models.firma).filter(models.firma.id == id).update({
        'nazwa': request.nazwa,
        'miasto': request.miasto,
        'ulica': request.ulica,
        'numer': request.numer,
        'kod_pocztowy': request.kod_pocztowy,
        'numer_telefonu': request.numer_telefonu
    })
    db.commit()
    return 'done'