from green_wind.crud.base import CRUDBase

from green_wind.schema.cell_conditions import (
    CellConditions,
    CellConditionsCreate,
    CellConditionsUpdate,
)


class CRUDCellConditions(
    CRUDBase[CellConditions, CellConditionsCreate, CellConditionsUpdate]
):
    pass


cell_conditions = CRUDCellConditions(CellConditions)
