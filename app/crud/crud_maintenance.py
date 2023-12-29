from app.crud.base import CRUDBase

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

        db_Maintenance_actions = []
        for action in obj_in.actions:
            action.Maintenance_id = db_model.id
            db_Maintenance_actions.append(self.create(db, obj_in=action))

        db_model.Maintenance_actions = db_Maintenance_actions
        return db_model


maintenance = CRUDMaintenance(Maintenance)
