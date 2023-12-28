from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, SQLModel, Relationship
from app.schema.schemas import TimestampSchema

if TYPE_CHECKING:
    from app.schema.status.status import Statuses


class FaultBase(TimestampSchema, SQLModel):
    fault_id: str
    fault_description: str
    fault_timestamp: str


class Fault(TimestampSchema, SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    fault_id: str
    fault_description: str
    fault_timestamp: str

    status_id: Optional[int] = Field(default=None, foreign_key="status.id")
    statuses: Optional["Statuses"] = Relationship(back_populates="faults")

    class Config:
        from_attributes = True


class FaultCreate(FaultBase):
    pass


class FaultRead(FaultBase):
    pass


class FaultReadOut(FaultRead):
    id: int


class FaultUpdate(FaultBase):
    pass
