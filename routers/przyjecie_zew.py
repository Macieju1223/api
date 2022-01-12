from fastapi import APIRouter, Depends
from database import get_db
import schem,models
from typing import List
from sqlalchemy.orm import Session

router = APIRouter(
    tags = ['Przyjecie zewnetrzne']
)

@router.get('/przyjecia_zewnetrzne')
def wyswietl_przyjecie_zew(db: Session = Depends(get_db)):
    zew = db.query(models.przyjecie).all()
    return zew

@router.get('/przyjecia_zewnetrzne/{numer_dokumentu}')
def wyswietl_przyjecie_po_id(numer_dokumentu,db: Session = Depends(get_db)):
    przyjecie = db.query(models.przyjecie).filter(models.przyjecie.numer_dokumentu == numer_dokumentu).first()
    return przyjecie

@router.post('/przyjecia_zewnetrzne')
def dodaj_przyjecie_zew(request: schem.przyjecie_zewnetrzne,db: Session = Depends(get_db)):
    new_przyjecie = models.przyjecie(
        numer_dokumentu = request.numer_dok,
        data_wystawienia = request.data_wyst,
        data_wydania = request.data_wyd,
        ilosc = request.ilosc,
        rabat = request.rabat,
        cena = request.cena
    )
    db.add(new_przyjecie)
    db.commit()
    db.refresh(new_przyjecie)
    return new_przyjecie

@router.put('/przyjecia_zewnetrzne/{numer_dokumentu}')
def edytuj_przyjecie_zewnetrzne(numer_dokumentu,request: schem.przyjecie_zewnetrzne,db: Session = Depends(get_db)):
    updated = db.query(models.przyjecie).filter(models.przyjecie.numer_dokumentu == numer_dokumentu).update({
        'data_wystawienia': request.data_wyst,
        'data_wydania': request.data_wyd,
        'ilosc': request.ilosc,
        'rabat': request.rabat,
        'cena': request.cena
    })
    db.commit()
    return updated

@router.delete('/przyjecia_zewnetrzne/{numer_dokumentu}')
def usun_przyjecie_zewnetrzne(numer_dokumentu,db: Session = Depends(get_db)):
    db.query(models.przyjecie).filter(models.przyjecie.numer_dokumentu == numer_dokumentu).delete(synchronize_session=False)
    db.commit()
    return 'dooone'