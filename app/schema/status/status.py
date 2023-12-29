from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Field, SQLModel, Relationship
from app.schema.schemas import TimestampSchema
from app.schema.status.fault import FaultCreate, Fault

if TYPE_CHECKING:
    from app.schema.battery_data import BatteryData


class StatusBase(SQLModel):
    state_of_charge: str
    health_status: str
    operational_status: str

    faults: List[FaultCreate] = []


class Status(TimestampSchema, SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    state_of_charge: str
    health_status: str
    operational_status: str
    faults: List["Fault"] = Relationship(back_populates="status")

    battery_data_id: Optional[int] = Field(default=None, foreign_key="batterydata.id")
    battery_data: Optional["BatteryData"] = Relationship(back_populates="status")

    class Config:
        from_attributes = True


class StatusCreate(StatusBase):
    pass


class StatusRead(StatusBase):
    faults: List[Fault] = []


class StatusReadOut(StatusRead):
    id: int


class StatusUpdate(StatusBase):
    pass
