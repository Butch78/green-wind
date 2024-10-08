from green_wind.crud.base import CRUDBase
from green_wind.schema.status.fault import Fault
from green_wind import crud

from green_wind.schema.status.status import Status, StatusCreate, StatusUpdate


class CRUDStatus(CRUDBase[Status, StatusCreate, StatusUpdate]):
    def create(self, db, *, obj_in) -> Status | None:
        db_model = Status.model_validate(obj_in.model_dump())
        db.add(db_model)
        db.commit()
        db.refresh(db_model)
        db_model

        db_faults = []
        for fault in obj_in.faults:
            fault = Fault(status_id=db_model.id, **fault.model_dump())
            db_faults.append(crud.fault.create(db, obj_in=fault))

        db_model.faults = db_faults
        return db_model


status = CRUDStatus(Status)
