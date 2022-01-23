from sqlalchemy.sql.schema import Index
from database import magazyn
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
# models definiuje tablice w db

class firma(magazyn):
    __tablename__ = 'firmy'
    id = Column(Integer,primary_key=True,index=True)
    nazwa = Column(String)
    miasto = Column(String)
    ulica = Column(String)
    numer = Column(String)
    kod_pocztowy = Column(Integer)
    numer_telefonu = Column(String)

class user(magazyn):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String)
    password = Column(String)
#--
class rosliny(magazyn):
    __tablename__ = 'rosliny'
    id_rosliny = Column(Integer,primary_key=True,index=True)
    nazwa = Column(String)
    polka_id = Column(Integer,ForeignKey('polki.id_polki'))
    
    creator = relationship('polki',back_populates='rosliny')
#--
class polki(magazyn):
    __tablename__ = 'polki'
    id_polki = Column(Integer,primary_key=True,index=True)
    sektor = Column(String)
    
    rosliny = relationship('rosliny',back_populates='creator')
#--
class partia(magazyn):
    __tablename__ = 'partia'
    id_partia = Column(Integer,primary_key=True,index=True)
    ilosc = Column(Integer)
    wartosc = Column(Integer)
    kod = Column(String)
#--
class pracownik(magazyn):
    __tablename__ = 'pracownicy'
    id_pracownik = Column(Integer,primary_key=True,index=True)
    imie = Column(String)
    nazwisko = Column(String)
    ulica = Column(String)
    numer = Column(Integer)
    miejscowosc = Column(String)
    kod_pocztowy = Column(Integer)
#--
class przyjecie(magazyn):
    __tablename__ = 'przyjecie_zewnetrzne'
    id_przyjecie = Column(Integer,primary_key=True,index=True)
    numer_dokumentu = Column(String)
    data_wystawienia = Column(String)
    data_wydania = Column(String)
    ilosc = Column(Integer)
    rabat = Column(Integer)
    cena = Column(Integer)
#--
class wydanie(magazyn):
    __tablename__ = 'wydanie_zewnetrzne'
    id_wydanie = Column(Integer,primary_key=True,index=True)
    numer_dokumentu = Column(String)
    data_wystawienia = Column(String)
    data_wydania = Column(String)
    ilosc = Column(Integer)
    rabat = Column(Integer)
    cena = Column(Integer)