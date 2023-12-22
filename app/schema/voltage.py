from SQLModel import Field, SQLModel
from app.schema.schemas import TimestampSchema


class Voltage(TimestampSchema, SQLModel):
    terminal_voltage: str
    operating_voltage: str
    charging_voltage: str


class Voltages(TimestampSchema, SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    terminal_voltage: str
    operating_voltage: str
    charging_voltage: str

    class Config:
        orm_mode = True


class VoltageCreate(Voltage):
    pass


class VoltageCreateOut(VoltageCreate):
    id: int


class VoltageRead(Voltage):
    pass


class VoltageUpdate(Voltage):
    pass
