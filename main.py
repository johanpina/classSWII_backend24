from fastapi import FastAPI
from schemas import User, UserBase
from schemas import Producto as ProductoEsquema
from database import engine, Session, get_db
from models import Base, Producto

from routers.user import users_router
from routers.products import products_router

from fastapi import Depends

app = FastAPI()

app.include_router(users_router)
app.include_router(products_router)

Base.metadata.create_all(engine) # Este comando es el que realiza la mágia

session = Session()

@app.get("/")
async def read_root():
    return {"Hello": "World"}









    



