from fastapi import FastAPI
import models
import uvicorn
from database import engine
from routers import firmy,urzytkownicy,polki,rosliny,partia,pracownicy,przyjecie_zew,wydania,authentication

app = FastAPI()

models.magazyn.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(firmy.router)
app.include_router(urzytkownicy.router)
app.include_router(polki.router)
app.include_router(rosliny.router)
app.include_router(partia.router)
app.include_router(pracownicy.router)
app.include_router(przyjecie_zew.router)
app.include_router(wydania.router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=True,
        port=8000
    )