from fastapi import FastAPI
import models
from database import engine
from routers import firmy,urzytkownicy,polki,rosliny,partia,pracownicy,przyjecie_zew,wydania

app = FastAPI()

models.magazyn.metadata.create_all(engine)

app.include_router(firmy.router)
app.include_router(urzytkownicy.router)
app.include_router(polki.router)
app.include_router(rosliny.router)
app.include_router(partia.router)
app.include_router(pracownicy.router)
app.include_router(przyjecie_zew.router)
app.include_router(wydania.router)
