from green_wind.crud.base import CRUDBase

from green_wind.schema.voltage import Voltage, VoltageCreate, VoltageUpdate


class CRUDVoltage(CRUDBase[Voltage, VoltageCreate, VoltageUpdate]):
    pass


voltage = CRUDVoltage(Voltage)
