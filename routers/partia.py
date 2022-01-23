from fastapi import APIRouter, Depends
from database import get_db
import schem,models
from typing import List
from sqlalchemy.orm import Session
from .oauth2 import get_current_user

router = APIRouter(
    tags = ['Partia']
)

@router.get('/partia')
def partie(db : Session = Depends(get_db),current_user: schem.login = Depends(get_current_user)):
    partie = db.query(models.partia).all()
    return partie

@router.post('/partia')
def dodaj_partie(request: schem.partia,db: Session = Depends(get_db),current_user: schem.login = Depends(get_current_user)):
    new_partia = models.partia(
        ilosc = request.ilosc,
        wartosc = request.wartosc,
        kod = request.kod
    )
    db.add(new_partia)
    db.commit()
    db.refresh(new_partia)
    return new_partia

@router.put('/partia/{kod}')
def edytuj_partie(kod,request: schem.partia,db: Session = Depends(get_db),current_user: schem.login = Depends(get_current_user)):
    db.query(models.partia).filter(models.partia.kod == kod).update({
       'ilosc': request.ilosc,
        'wartosc': request.wartosc
    })
    db.commit()
    return 'done and done'
    
@router.delete('/partia/{kod}')
def usun_partie(kod,db: Session = Depends(get_db),current_user: schem.login = Depends(get_current_user)):
    db.query(models.partia).filter(models.partia.kod == kod).delete(synchronize_session=False)
    db.commit()
    return 'deleted i quess'