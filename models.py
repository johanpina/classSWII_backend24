from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Cliente(Base):
    __tablename__ = 'Clientes'
    ID_Cliente = Column(Integer, primary_key=True)
    Nombre = Column(String)
    Apellido = Column(String)
    Email = Column(String, unique=True)
    Telefono = Column(String)

class Categoria(Base):
    __tablename__ = 'Categorias'
    ID_Categoria = Column(Integer, primary_key=True)
    Nombre = Column(String, unique=True)

class Producto(Base):
    __tablename__ = 'Productos'
    ID_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String)
    Precio = Column(Float)
    Cantidad = Column(Integer)
    ID_Categoria = Column(Integer, ForeignKey('Categorias.ID_Categoria'))
    categoria = relationship("Categoria")

class Empleado(Base):
    __tablename__ = 'Empleados'
    ID_Empleado = Column(Integer, primary_key=True)
    Nombre = Column(String)
    Apellido = Column(String)
    Cargo = Column(String)

class Venta(Base):
    __tablename__ = 'Ventas'
    ID_Venta = Column(Integer, primary_key=True)
    Fecha = Column(Date)
    ID_Cliente = Column(Integer, ForeignKey('Clientes.ID_Cliente'))
    ID_Empleado = Column(Integer, ForeignKey('Empleados.ID_Empleado'))
    cliente = relationship("Cliente")
    empleado = relationship("Empleado")

class DetalleVenta(Base):
    __tablename__ = 'DetallesVenta'
    ID_Detalle = Column(Integer, primary_key=True)
    ID_Venta = Column(Integer, ForeignKey('Ventas.ID_Venta'))
    ID_Producto = Column(Integer, ForeignKey('Productos.ID_Producto'))
    Cantidad = Column(Integer)
    Precio_Unitario = Column(Float)
    venta = relationship("Venta")
    producto = relationship("Producto")