from app.crud.base import CRUDBase

from app.schema.temperature import Temperature, TemperatureCreate, TemperatureUpdate


class CRUDTemperature(CRUDBase[Temperature, TemperatureCreate, TemperatureUpdate]):
    pass


temperature = CRUDTemperature(Temperature)
