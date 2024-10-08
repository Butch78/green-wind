from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, SQLModel, Relationship
from green_wind.schema.schemas import TimestampSchema

if TYPE_CHECKING:
    from green_wind.schema.battery_data import BatteryData


class EnvironmentalConditionsBase(SQLModel):
    ambient_temperature: str
    humidity: str
    altitude: str
    pressure: str


class EnvironmentalCondition(TimestampSchema, EnvironmentalConditionsBase, table=True):
    id: int = Field(default=None, primary_key=True)

    battery_data_id: Optional[int] = Field(default=None, foreign_key="batterydata.id")
    battery_data: Optional["BatteryData"] = Relationship(
        back_populates="environmental_conditions"
    )

    class Config:
        from_attributes = True


class EnvironmentalConditionsCreate(EnvironmentalConditionsBase):
    pass


class EnvironmentalConditionsRead(EnvironmentalConditionsBase):
    pass


class EnvironmentalConditionsReadOut(EnvironmentalConditionsRead):
    id: int


class EnvironmentalConditionsUpdate(EnvironmentalConditionsBase):
    pass
