from datetime import datetime
from typing import Optional
from sqlmodel import Field, Relationship, SQLModel
from green_wind.schema.capacity import Capacity, CapacityCreate
from green_wind.schema.current import Current, CurrentCreate
from green_wind.schema.energy_throughput import EnergyThroughput, EnergyThroughputCreate
from green_wind.schema.environmental_conditions import (
    EnvironmentalCondition,
    EnvironmentalConditionsCreate,
)
from green_wind.schema.maintenance.maintenance import Maintenance, MaintenanceCreate
from green_wind.schema.operational_parameters import (
    OperationalParameter,
    OperationalParametersCreate,
)
from green_wind.schema.schemas import TimestampSchema
from green_wind.schema.status.status import Status, StatusCreate
from green_wind.schema.temperature import Temperature, TemperatureCreate
from green_wind.schema.voltage import Voltage, VoltageCreate


class BatteryDataBase(SQLModel):
    battery_id: str
    manufacturer: str
    model: str
    timestamp: datetime

    capacity: CapacityCreate
    voltage: VoltageCreate
    temperature: TemperatureCreate
    current: CurrentCreate
    status: StatusCreate
    energy_throughput: EnergyThroughputCreate
    maintenance: MaintenanceCreate
    environmental_conditions: EnvironmentalConditionsCreate
    operational_parameters: OperationalParametersCreate


class BatteryData(TimestampSchema, SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    battery_id: str
    manufacturer: str
    model: str
    timestamp: datetime

    capacity: Optional["Capacity"] = Relationship(back_populates="battery_data")
    voltage: Optional["Voltage"] = Relationship(back_populates="battery_data")
    temperature: Optional["Temperature"] = Relationship(back_populates="battery_data")
    current: Optional["Current"] = Relationship(back_populates="battery_data")
    status: Optional["Status"] = Relationship(back_populates="battery_data")
    energy_throughput: Optional["EnergyThroughput"] = Relationship(
        back_populates="battery_data"
    )
    maintenance: Optional["Maintenance"] = Relationship(back_populates="battery_data")
    environmental_conditions: Optional["EnvironmentalCondition"] = Relationship(
        back_populates="battery_data"
    )
    operational_parameters: Optional["OperationalParameter"] = Relationship(
        back_populates="battery_data"
    )

    class Config:
        from_attributes = True


class BatteryDataCreate(BatteryDataBase):
    pass


class BatteryDataRead(BatteryDataBase):
    pass


class BatteryDataReadOut(BatteryDataRead):
    id: int


class BatteryDataUpdate(BatteryDataBase):
    pass
