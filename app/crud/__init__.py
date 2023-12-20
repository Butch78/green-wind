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
from app.schema.deposit_rate import DepositRates, DepositRatesCreate, DepositRatesUpdate

from app.schema.target_range import TargetRanges, TargetRangesCreate, TargetRangesUpdate
from app.schema.target_rate import TargetRates, TargetRatesCreate, TargetRatesUpdate


deposit_rates = CRUDBase[DepositRates, DepositRatesCreate, DepositRatesUpdate](
    DepositRates
)
target_ranges = CRUDBase[TargetRanges, TargetRangesCreate, TargetRangesUpdate](
    TargetRanges
)
target_rates = CRUDBase[TargetRates, TargetRatesCreate, TargetRatesUpdate](TargetRates)
