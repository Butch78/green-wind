from app.crud.base import CRUDBase

from app.schema.cell_conditions import (CellConditions, CellConditionsCreate, CellConditionsUpdate)

class CRUDCellConditions(CRUDBase[CellConditions, CellConditionsCreate, CellConditionsUpdate]):
    pass

cell_conditions = CRUDCellConditions(CellConditions)