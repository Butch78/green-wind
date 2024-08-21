from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Field, SQLModel, Relationship
from green_wind.schema.schemas import TimestampSchema
from green_wind.schema.maintenance.maintenance_action import (
    MaintenanceAction,
    MaintenanceActionCreate,
)
from datetime import date

if TYPE_CHECKING:
    from green_wind.schema.battery_data import BatteryData


class MaintenanceBase(SQLModel):
    last_maintenance_date: date
    next_maintenance_due: date
    maintenance_actions: List[MaintenanceActionCreate] = []


class Maintenance(TimestampSchema, SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    last_maintenance_date: date
    next_maintenance_due: date
    maintenance_actions: List["MaintenanceAction"] = Relationship(
        back_populates="maintenance"
    )

    battery_data_id: Optional[int] = Field(default=None, foreign_key="batterydata.id")
    battery_data: Optional["BatteryData"] = Relationship(back_populates="maintenance")

    class Config:
        from_attributes = True


class MaintenanceCreate(MaintenanceBase):
    pass


class MaintenanceRead(MaintenanceBase):
    pass


class MaintenanceReadOut(MaintenanceBase):
    id: int


class MaintenanceUpdate(MaintenanceBase):
    pass
