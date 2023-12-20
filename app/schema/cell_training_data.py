from sqlmodel import SQLModel, Field


class CellTrainingData(SQLModel):
    folder_name: str = Field(..., description="File name")
    x_train: int = Field(..., description="Cell cycle")
    y_train: float = Field(..., description="Cell voltage")
    static_cell_voltage: float = Field(..., description="Static cell voltage")


class CellTrainingDatas(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    folder_name: str = Field(..., description="File name")
    x_train: int = Field(..., description="Cell cycle")
    y_train: float = Field(..., description="Cell voltage")
    static_cell_voltage: float = Field(..., description="Static cell voltage")

    class Config:
        orm_mode = True


class CellDataTrainingCreate(CellTrainingData):
    pass


class CellDataCreateOut(CellDataTrainingCreate):
    id: int


class CellDataRead(CellTrainingData):
    pass


class CellDataUpdate(CellTrainingData):
    pass
