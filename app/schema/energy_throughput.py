from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, SQLModel, Relationship
from app.schema.schemas import TimestampSchema

if TYPE_CHECKING:
    from app.schema.battery_data import BatteryData


class EnergyThroughputBase(TimestampSchema, SQLModel):
    total_energy_delivered: str
    total_energy_charged: str


class EnergyThroughput(TimestampSchema, SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    total_energy_delivered: str
    total_energy_charged: str

    battery_data_id: Optional[int] = Field(default=None, foreign_key="batterydata.id")
    battery_data: Optional["BatteryData"] = Relationship(
        back_populates="energy_throughputs"
    )

    class Config:
        from_attributes = True


class EnergyThroughputCreate(EnergyThroughputBase):
    pass


class EnergyThroughputRead(EnergyThroughputBase):
    pass


class EnergyThroughputReadOut(EnergyThroughputBase):
    id: int


class EnergyThroughputUpdate(EnergyThroughputBase):
    pass
