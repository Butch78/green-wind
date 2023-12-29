from app.crud.base import CRUDBase

from app.schema.cell_training_data import (
    CellTrainingDatas,
    CellDataTrainingCreate,
    CellDataUpdate,
)


class CRUDCellTrainingData(
    CRUDBase[CellTrainingDatas, CellDataTrainingCreate, CellDataUpdate]
):
    pass


cell_training_data = CRUDCellTrainingData(CellTrainingDatas)
