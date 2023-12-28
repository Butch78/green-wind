from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel
from app.schema.capacity import Capacity
from app.schema.current import Current
from app.schema.energy_throughput import EnergyThroughput
from app.schema.environmental_conditions import EnvironmentalCondition
from app.schema.maintence.maintence import Maintenance
from app.schema.operational_parameters import OperationalParameter
from app.schema.schemas import TimestampSchema
from app.schema.status.status import Status
from app.schema.temperature import Temperature
from app.schema.voltage import Voltage


class BatteryDataBase(TimestampSchema, SQLModel):
    battery_id: str
    manufacturer: str
    model: str
    timestamp: str


class BatteryData(TimestampSchema, SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    battery_id: str
    manufacturer: str
    model: str
    timestamp: str

    capacity: Optional["Capacity"] = Relationship(back_populates="batterydata")
    voltage: Optional["Voltage"] = Relationship(back_populates="batterydata")
    temperature: Optional["Temperature"] = Relationship(back_populates="batterydata")
    current: Optional["Current"] = Relationship(back_populates="batterydata")
    status: Optional["Status"] = Relationship(back_populates="batterydata")
    energy_throughput: Optional["EnergyThroughput"] = Relationship(
        back_populates="batterydata"
    )
    maintenance: Optional[Maintenance] = Relationship(back_populates="batterydata")
    environmental_conditions: Optional[EnvironmentalCondition] = Relationship(
        back_populates="batterydata"
    )
    operational_parameters: Optional[OperationalParameter] = Relationship(
        back_populates="batterydata"
    )

    class Config:
        from_attributes = True


class BatteryDataCreate(BatteryDataBase):
    pass


class BatteryDataRead(BatteryDataBase):
    capacities: List[Capacity] = []
    voltages: List[Voltage] = []
    temperatures: List[Temperature] = []
    currents: List[Current] = []
    statuses: List[Status] = []
    energy_throughputs: List[EnergyThroughput] = []
    maintenances: List[Maintenance] = []
    environmental_conditions: List[EnvironmentalCondition] = []
    operational_parameters: List[OperationalParameter] = []


class BatteryDataReadOut(BatteryDataRead):
    id: int


class BatteryDataUpdate(BatteryDataBase):
    pass
