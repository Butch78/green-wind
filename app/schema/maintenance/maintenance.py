from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Field, SQLModel, Relationship
from app.schema.schemas import TimestampSchema
from app.schema.maintenance.maintenance_action import MaintenanceAction

if TYPE_CHECKING:
    from app.schema.battery_data import BatteryData


class MaintenanceBase(SQLModel):
    last_maintenance_date: str
    next_maintenance_due: str
    maintenance_actions: List[MaintenanceAction] = []


class Maintenance(TimestampSchema, SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    last_maintenance_date: str
    next_maintenance_due: str
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
