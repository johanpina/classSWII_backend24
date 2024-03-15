from fastapi import APIRouter, Depends
from schemas import Producto as ProductoEsquema
from database import Session, get_db
from models import Producto


products_router = APIRouter(prefix="/productos", tags=["productos"])

@products_router.post("/")
async def create_producto(nuevo_producto: ProductoEsquema, db: Session =  Depends(get_db)) -> ProductoEsquema:
    new = Producto(**nuevo_producto.dict())
    db.add(new)
    db.commit()
    return new
