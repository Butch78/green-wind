from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, SQLModel, Relationship
from app.schema.schemas import TimestampSchema

if TYPE_CHECKING:
    from app.schema.maintence.maintence import Maintenance


class MaintenanceActionBase(TimestampSchema, SQLModel):
    action_id: str
    action_description: str
    action_status: str


class MaintenceAction(TimestampSchema, SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    action_id: str
    action_description: str
    action_status: str

    maintence_id: Optional[int] = Field(default=None, foreign_key="maintenance.id")
    maintenance: Optional["Maintenance"] = Relationship(
        back_populates="maintence_actions"
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
