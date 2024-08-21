from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field


class CellConditionsBase(SQLModel):
    barcode: str = Field(..., description="Cell barcode")
    dataset: str = Field(..., description="Dataset")
    batch_date: datetime = Field(..., description="Batch date")
    cycle_life: int = Field(..., description="Cycle life")
    charging_policy: str = Field(..., description="Charging policy")
    c1: float = Field(..., description="c1")
    percent: int = Field(..., description="percent")
    c2: float = Field(..., description="c2")


class CellConditions(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    barcode: str = Field(..., description="Cell barcode")
    dataset: str = Field(..., description="Dataset")
    batch_date: datetime = Field(..., description="Batch date")
    cycle_life: int = Field(..., description="Cycle life")
    charging_policy: str = Field(..., description="Charging policy")
    c1: float = Field(..., description="c1")
    percent: int = Field(..., description="percent")
    c2: float = Field(..., description="c2")

    class ConfigDict:
        from_attributes = True


class CellConditionsCreate(CellConditionsBase):
    pass


class CellConditionsCreateOut(CellConditionsCreate):
    id: int


class CellConditionsRead(CellConditionsBase):
    pass


class CellConditionsUpdate(CellConditionsBase):
    pass
