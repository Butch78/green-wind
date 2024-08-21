from sqlmodel import SQLModel, Field
from green_wind.schema.schemas import TimestampSchema


class CellTrainingDataBase(SQLModel):
    folder_name: str = Field(..., description="File name")
    x_train: int = Field(..., description="Cell cycle")
    y_train: float = Field(..., description="Cell voltage")
    static_cell_voltage: float = Field(..., description="Static cell voltage")


class CellTrainingDatas(TimestampSchema, SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    folder_name: str = Field(..., description="File name")
    x_train: int = Field(..., description="Cell cycle")
    y_train: float = Field(..., description="Cell voltage")
    static_cell_voltage: float = Field(..., description="Static cell voltage")

    class Config:
        from_attributes = True


class CellDataTrainingCreate(CellTrainingDataBase):
    pass


class CellDataCreateOut(CellDataTrainingCreate):
    id: int


class CellDataRead(CellTrainingDataBase):
    pass


class CellDataUpdate(CellTrainingDataBase):
    pass
