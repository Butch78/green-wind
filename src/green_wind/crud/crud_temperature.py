from green_wind.crud.base import CRUDBase

from green_wind.schema.temperature import (
    Temperature,
    TemperatureCreate,
    TemperatureUpdate,
)


class CRUDTemperature(CRUDBase[Temperature, TemperatureCreate, TemperatureUpdate]):
    pass


temperature = CRUDTemperature(Temperature)
