from app.crud.base import CRUDBase

from app.schema.battery_data import BatteryData, BatteryDataCreate, BatteryDataUpdate


class CRUDBatteryData(CRUDBase[BatteryData, BatteryDataCreate, BatteryDataUpdate]):
    pass


battery_data = CRUDBatteryData(BatteryData)
