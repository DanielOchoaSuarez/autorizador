from marshmallow import Schema, fields
from sqlalchemy import Column, String

from src.models.model import Model
from src.models.db import Base


class DeporteEntity(Model, Base):
    __tablename__ = 'deporte'
    nombre = Column(String)

    # Constructor
    def __init__(self, nombre):
        Model.__init__(self)
        self.nombre = nombre


# Campos que estarán presentes al serializar el objeto como JSON
class DeporteJsonSchema(Schema):
    id = fields.String()
    nombre = fields.String()
