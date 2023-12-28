from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, SQLModel, Relationship
from app.schema.schemas import TimestampSchema


if TYPE_CHECKING:
    from app.schema.battery_data import BatteryData


class OperationalParametersBase(TimestampSchema, SQLModel):
    charge_cycles: str
    discharge_cycles: str
    max_continuous_discharge_rate: str
    max_continuous_charge_rate: str


class OperationalParameter(TimestampSchema, SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    charge_cycles: str
    discharge_cycles: str
    max_continuous_discharge_rate: str
    max_continuous_charge_rate: str

    battery_data_id: Optional[int] = Field(default=None, foreign_key="batterydata.id")
    battery_data: Optional["BatteryData"] = Relationship(
        back_populates="operational_parameters"
    )

    class Config:
        from_attributes = True


class OperationalParametersCreate(OperationalParametersBase):
    pass


class OperationalParametersRead(OperationalParametersBase):
    pass


class OperationalParametersReadOut(OperationalParametersBase):
    id: int


class OperationalParametersUpdate(OperationalParametersBase):
    pass
