from app.crud.base import CRUDBase

from app.schema.cell_conditions import (
    CellConditions,
    CellConditionsCreate,
    CellConditionsUpdate,
)
from app.schema.cell_training_data import (
    CellTrainingDatas,
    CellDataTrainingCreate,
    CellDataUpdate,
)

cell_conditions = CRUDBase[CellConditions, CellConditionsCreate, CellConditionsUpdate](
    CellConditions
)
cell_training_data = CRUDBase[
    CellTrainingDatas, CellDataTrainingCreate, CellDataUpdate
](CellTrainingDatas)


from app.crud.crud_battery_data import (
    battery_data,
)

from app.schema.battery_data import (
    BatteryData,
    BatteryDataCreate,
    BatteryDataUpdate,
)

battery_data = CRUDBase[battery_data, BatteryDataCreate, BatteryDataUpdate](BatteryData)
