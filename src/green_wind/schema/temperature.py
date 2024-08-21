from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, SQLModel, Relationship
from green_wind.schema.schemas import TimestampSchema

if TYPE_CHECKING:
    from green_wind.schema.battery_data import BatteryData


class TemperatureBase(SQLModel):
    internal_temperature: str
    external_temperature: str
    operating_temperature_range: str


class Temperature(TimestampSchema, TemperatureBase, table=True):
    id: int = Field(default=None, primary_key=True)

    battery_data_id: Optional[int] = Field(default=None, foreign_key="batterydata.id")
    battery_data: Optional["BatteryData"] = Relationship(back_populates="temperature")

    class Config:
        from_attributes = True


class TemperatureCreate(TemperatureBase):
    pass


class TemperatureRead(TemperatureBase):
    pass


class TemperatureReadOut(TemperatureRead):
    pass


class TemperatureUpdate(TemperatureBase):
    pass
