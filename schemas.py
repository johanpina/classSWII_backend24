from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str
    # Le dice a fastapi que es de un modelo de ORM
    class Config:
        orm_mode = True

class User(UserBase):
    password: str


class Cliente(BaseModel):
    ID_Cliente: int
    Nombre: str
    Apellido: str
    Email: str
    Telefono: str

    # Le dice a fastapi que es de un modelo de ORM
    class Config:
        orm_mode = True
class Categoria(BaseModel):
    ID_Categoria: int
    Nombre: str

    # Le dice a fastapi que es de un modelo de ORM
    class Config:
        orm_mode = True

class Producto(BaseModel):

    Nombre: str
    Precio: float
    Cantidad: int
    ID_Categoria: int

    # Le dice a fastapi que es de un modelo de ORM
    class Config:
        orm_mode = True

class Empleado(BaseModel):
    ID_Empleado: int
    Nombre: str
    Apellido: str
    Cargo: str

    # Le dice a fastapi que es de un modelo de ORM
    class Config:
        orm_mode = True
    
class Venta(BaseModel):
    ID_Venta: int
    Fecha: str
    ID_Cliente: int
    ID_Empleado: int

    # Le dice a fastapi que es de un modelo de ORM
    class Config:
        orm_mode = True

class DetalleVenta(BaseModel):
    ID_Detalle: int
    ID_Venta: int
    ID_Producto: int
    Cantidad: int
    Precio_Unitario: float

    # Le dice a fastapi que es de un modelo de ORM
    class Config:
        orm_mode = True
