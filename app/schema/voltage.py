from typing import TYPE_CHECKING, Optional

from sqlmodel import Relationship
from sqlmodel import Field, SQLModel
from app.schema.schemas import TimestampSchema

if TYPE_CHECKING:
    from app.schema.battery_data import BatteryData


class VoltageBase(SQLModel):
    terminal_voltage: str
    operating_voltage: str
    charging_voltage: str


class Voltage(TimestampSchema, VoltageBase, table=True):
    id: int = Field(default=None, primary_key=True)

    battery_data_id: Optional[int] = Field(default=None, foreign_key="batterydata.id")
    battery_data: Optional["BatteryData"] = Relationship(back_populates="voltage")

    class Config:
        from_attributes = True


class VoltageCreate(VoltageBase):
    pass


class VoltageCreateOut(VoltageCreate):
    id: int


class VoltageRead(VoltageBase):
    pass


class VoltageUpdate(VoltageBase):
    pass
