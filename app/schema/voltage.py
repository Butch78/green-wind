from typing import TYPE_CHECKING, Optional

from sqlmodel import Relationship
from sqlmodel import Field, SQLModel
from app.schema.schemas import TimestampSchema

if TYPE_CHECKING:
    from app.schema.battery_data import BatteryData


class VoltageBase(TimestampSchema, SQLModel):
    terminal_voltage: str
    operating_voltage: str
    charging_voltage: str

    battery_data_id: Optional[int]


class Voltage(TimestampSchema, SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    terminal_voltage: str
    operating_voltage: str
    charging_voltage: str

    battery_data_id: Optional[int] = Field(default=None, foreign_key="batterydata.id")
    battery_data: Optional["BatteryData"] = Relationship(back_populates="voltages")

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
