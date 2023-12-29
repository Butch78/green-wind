from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, SQLModel, Relationship
from app.schema.schemas import TimestampSchema

if TYPE_CHECKING:
    from app.schema.battery_data import BatteryData


class CurrentBase(SQLModel):
    charging_current: str
    discharging_current: str
    operating_current_range: str


class Current(TimestampSchema, SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    charging_current: str
    discharging_current: str
    operating_current_range: str

    battery_data_id: Optional[int] = Field(default=None, foreign_key="batterydata.id")
    battery_data: Optional["BatteryData"] = Relationship(back_populates="current")

    class Config:
        from_attributes = True


class CurrentCreate(CurrentBase):
    pass


class CurrentRead(CurrentBase):
    pass


class CurrentReadOut(CurrentBase):
    id: int


class CurrentUpdate(CurrentBase):
    pass
