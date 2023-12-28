from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, SQLModel
from app.schema.schemas import TimestampSchema

if TYPE_CHECKING:
    from app.schema.battery_data import BatteryData


class CapacityBase(TimestampSchema, SQLModel):
    current_capacity: str
    design_capacity: str
    remaining_capacity: str


class Capacity(TimestampSchema, SQLModel):
    id: int = Field(default=None, primary_key=True)
    current_capacity: str
    design_capacity: str
    remaining_capacity: str

    battery_data_id: Optional[int] = Field(default=None, foreign_key="batterydata.id")
    battery_data: Optional["BatteryData"] = Relationship(back_populates="capacities")

    class Config:
        from_attributes = True


class CapacityCreate(CapacityBase):
    pass


class CapacityRead(CapacityBase):
    pass


class CapacityReadOut(CapacityBase):
    pass


class CapacityUpdate(CapacityBase):
    pass
