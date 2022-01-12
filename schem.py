from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import Numeric

class firma(BaseModel):
    nazwa: str
    miasto: str
    ulica: str
    numer: int
    kod_pocztowy: int
    numer_telefonu: int

class podstawowe_informacje(BaseModel):
    nazwa: str
    numer: int
    class Config():
        orm_mode = True
#--
class login(BaseModel):
    login: str
    haslo: str
class urzytkownicy(BaseModel):
    login: str
    class Config():
        orm_mode = True
#--
class polka(BaseModel):
    sektor: str
    class Config():
        orm_mode = True
#--
class rosliny(BaseModel):
    nazwa: str
class roslina_id(BaseModel):
    nazwa: str
    creator: polka
    class Config():
        orm_mode = True
#--
class partia(BaseModel):
    ilosc: int
    wartosc: int
    kod: str
#--
class pracownicy(BaseModel):
    imie: str
    nazwisko: str
    ulica: str
    numer: int
    miejscowosc: str
    kod_pocztowy: int
#--
class przyjecie_zewnetrzne(BaseModel):
    numer_dok: str
    data_wyst: str
    data_wyd: str
    ilosc: int
    rabat: int
    cena: int
#--
class wydanie_zewnetrzne(BaseModel):
    numer_dok: str
    data_wyst: str
    data_wyd: str
    ilosc: int
    rabat: int
    cena: int