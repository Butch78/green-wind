from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, SQLModel, Relationship
from app.schema.schemas import TimestampSchema

if TYPE_CHECKING:
    from app.schema.battery_data import BatteryData


class EnvironmentalConditionsBase(TimestampSchema, SQLModel):
    ambient_temperature: str
    humidity: str
    altitude: str
    pressure: str


class EnvironmentalCondition(TimestampSchema, SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    ambient_temperature: str
    humidity: str
    altitude: str
    pressure: str

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
