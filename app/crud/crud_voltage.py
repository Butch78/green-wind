from app.crud.base import CRUDBase

from app.schema.voltage import Voltage, VoltageCreate, VoltageUpdate


class CRUDVoltage(CRUDBase[Voltage, VoltageCreate, VoltageUpdate]):
    pass


voltage = CRUDVoltage(Voltage)
