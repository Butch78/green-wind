from pydantic import BaseModel
from sqlmodel import SQLModel

from app.schema.schemas import TimestampSchema
from app.schema.voltage import Voltage


class Capacity(BaseModel):
    current_capacity: str
    design_capacity: str
    remaining_capacity: str


class Temperature(BaseModel):
    internal_temperature: str
    external_temperature: str
    operating_temperature_range: str


class Current(BaseModel):
    charging_current: str
    discharging_current: str
    operating_current_range: str


class Status(BaseModel):
    state_of_charge: str
    health_status: str
    operational_status: str
    faults: list[str]


class EnergyThroughput(BaseModel):
    total_energy_delivered: str
    total_energy_charged: str


class MaintenanceAction(BaseModel):
    action_id: str
    action_description: str
    action_status: str


class Maintenance(BaseModel):
    last_maintenance_date: str
    next_maintenance_due: str
    maintenance_actions: list[MaintenanceAction]


class EnvironmentalConditions(BaseModel):
    ambient_temperature: str
    humidity: str
    altitude: str


class OperationalParameters(BaseModel):
    charge_cycles: str
    discharge_cycles: str
    max_continuous_discharge_rate: str
    max_continuous_charge_rate: str


class BatteryData(TimestampSchema, SQLModel):
    battery_id: str
    manufacturer: str
    model: str
    capacity: Capacity
    voltage: Voltage
    temperature: Temperature
    current: Current
    status: Status
    energy_throughput: EnergyThroughput
    maintenance: Maintenance
    environmental_conditions: EnvironmentalConditions
    operational_parameters: OperationalParameters
    timestamp: str
