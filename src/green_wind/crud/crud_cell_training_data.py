from green_wind.crud.base import CRUDBase

from green_wind.schema.cell_training_data import (
    CellTrainingDatas,
    CellDataTrainingCreate,
    CellDataUpdate,
)


class CRUDCellTrainingData(
    CRUDBase[CellTrainingDatas, CellDataTrainingCreate, CellDataUpdate]
):
    pass


cell_training_data = CRUDCellTrainingData(CellTrainingDatas)
