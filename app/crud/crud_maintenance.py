from app.crud.base import CRUDBase
from app import crud

from app.schema.maintenance.maintenance import (
    Maintenance,
    MaintenanceCreate,
    MaintenanceUpdate,
)


class CRUDMaintenance(CRUDBase[Maintenance, MaintenanceCreate, MaintenanceUpdate]):
    def create(self, db, *, obj_in) -> Maintenance | None:
        db_model = Maintenance.model_validate(obj_in.model_dump())
        db.add(db_model)
        db.commit()
        db.refresh(db_model)

        db_maintenance_actions = []
        for action in obj_in.maintenance_actions:
            action.maintenance_id = db_model.id
            db_maintenance_actions.append(crud.maintenance_action.create(db, obj_in=action))

        db_model.maintenance_actions = db_maintenance_actions
        return db_model


maintenance = CRUDMaintenance(Maintenance)
