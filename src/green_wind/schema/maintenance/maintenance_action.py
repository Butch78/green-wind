from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, SQLModel, Relationship
from green_wind.schema.schemas import TimestampSchema

if TYPE_CHECKING:
    from green_wind.schema.maintenance.maintenance import Maintenance


class MaintenanceActionBase(SQLModel):
    action_id: str
    action_description: str
    action_status: str


class MaintenanceAction(TimestampSchema, MaintenanceActionBase, table=True):
    id: int = Field(default=None, primary_key=True)

    maintenance_id: Optional[int] = Field(default=None, foreign_key="maintenance.id")
    maintenance: Optional["Maintenance"] = Relationship(
        back_populates="maintenance_actions"
    )

    class Config:
        from_attributes = True


class MaintenanceActionCreate(MaintenanceActionBase):
    pass


class MaintenanceActionRead(MaintenanceActionBase):
    pass


class MaintenanceActionReadOut(MaintenanceActionRead):
    id: int


class MaintenanceActionUpdate(MaintenanceActionBase):
    pass
