from fastapi import APIRouter, Depends
from database import get_db
import schem,models
from typing import List
from sqlalchemy.orm import Session

router = APIRouter(
    tags = ['Pracownicy']
)

@router.get('/pracownicy')
def wyswietl_niewolnika(db: Session = Depends(get_db)):
    pracownicy = db.query(models.pracownik).all()
    return pracownicy

@router.post('/pracownicy')
def dodaj_niewolnika(request: schem.pracownicy,db: Session = Depends(get_db)):
    new_niewolnik = models.pracownik(
        imie = request.imie,
        nazwisko = request.nazwisko,
        ulica = request.ulica,
        numer = request.numer,
        miejscowosc = request.miejscowosc,
        kod_pocztowy = request.kod_pocztowy
    )
    db.add(new_niewolnik)
    db.commit()
    db.refresh(new_niewolnik)
    return new_niewolnik

@router.put('/pracownicy/{numer}')
def edytuj_niewolnika(numer,request: schem.pracownicy,db: Session = Depends(get_db)):
    db.query(models.pracownik).filter(models.pracownik.numer == numer).update({
        'imie': request.imie,
        'nazwisko': request.nazwisko,
        'ulica': request.ulica,
        'miejscowosc': request.miejscowosc,
        'kod_pocztowy': request.kod_pocztowy
    })
    db.commit()
    return 'done and done'

@router.delete('/pracownicy/{numer}')
def usun_pracownika(numer,db: Session = Depends(get_db)):
    db.query(models.pracownik).filter(models.pracownik.numer == numer).delete(synchronize_session=False)
    db.commit()
    return 'dooone'