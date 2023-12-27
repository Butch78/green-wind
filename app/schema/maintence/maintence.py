from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Field, SQLModel, Relationship
from app.schema.schemas import TimestampSchema
from app.schema.maintence.maintence_action import MaintenceAction

if TYPE_CHECKING:
    from app.schema.battery_data import BatteryData


class MaintenanceBase(SQLModel):
    action_id: str
    action_description: str
    action_status: str
    maintence_actions: List[MaintenceAction] = []


class Maintenance(TimestampSchema, SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    action_id: str
    action_description: str
    action_status: str
    maintence_actions: List["MaintenceAction"] = Relationship(
        back_populates="maintenances"
    )

    battery_data_id: Optional[int] = Field(default=None, foreign_key="batterydata.id")
    battery_data: Optional["BatteryData"] = Relationship(back_populates="maintenances")

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
