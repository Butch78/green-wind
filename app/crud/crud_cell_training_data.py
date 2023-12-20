from app.crud.base import CRUDBase

from app.schema.cell_training_data import (
    CellTrainingData,
    CellDataTrainingCreate,
    CellDataUpdate,
)


class CRUDCellTrainingData(
    CRUDBase[CellTrainingData, CellDataTrainingCreate, CellDataUpdate]
):
    pass


cell_training_data = CRUDCellTrainingData(CellTrainingData)
