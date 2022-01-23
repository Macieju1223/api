from fastapi import APIRouter, Depends
from database import get_db
import schem,models
from sqlalchemy.orm import Session
from .oauth2 import get_current_user

router = APIRouter(
    tags = ['Wydania Zewnetrzne']
)

@router.get('/wydanie_zewnetrzne')
def wyswietl_wydanie_zew(db: Session = Depends(get_db),current_user: schem.login = Depends(get_current_user)):
    zew = db.query(models.wydanie).all()
    return zew

@router.get('/wydanie_zewnetrzne/{numer_dokumentu}')
def wyswietl_przyjecie_po_id(numer_dokumentu,db: Session = Depends(get_db)):
    wydanie = db.query(models.wydanie).filter(models.wydanie.numer_dokumentu == numer_dokumentu).first()
    return wydanie

@router.post('/wydanie_zewnetrzne')
def dodaj_wydanie_zew(request: schem.wydanie_zewnetrzne,db: Session = Depends(get_db),current_user: schem.login = Depends(get_current_user)):
    new_wydanie = models.wydanie(
        numer_dokumentu = request.numer_dok,
        data_wystawienia = request.data_wyst,
        data_wydania = request.data_wyd,
        ilosc = request.ilosc,
        rabat = request.rabat,
        cena = request.cena
    )
    db.add(new_wydanie)
    db.commit()
    db.refresh(new_wydanie)
    return new_wydanie

@router.put('/wydanie_zewnetrzne/{numer_dokumentu}')
def edytuj_przyjecie_zewnetrzne(numer_dokumentu,request: schem.wydanie_zewnetrzne,db: Session = Depends(get_db),current_user: schem.login = Depends(get_current_user)):
    updated = db.query(models.wydanie).filter(models.wydanie.numer_dokumentu == numer_dokumentu).update({
        'data_wystawienia': request.data_wyst,
        'data_wydania': request.data_wyd,
        'ilosc': request.ilosc,
        'rabat': request.rabat,
        'cena': request.cena
    })
    db.commit()
    return updated

@router.delete('/wydanie_zewnetrzne/{numer_dokumentu}')
def usun_wydanie_zewnetrzne(numer_dokumentu,db: Session = Depends(get_db),current_user: schem.login = Depends(get_current_user)):
    db.query(models.wydanie).filter(models.wydanie.numer_dokumentu == numer_dokumentu).delete(synchronize_session=False)
    db.commit()
    return 'dooone'