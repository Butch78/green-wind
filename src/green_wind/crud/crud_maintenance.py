from green_wind.crud.base import CRUDBase
from green_wind import crud

from green_wind.schema.maintenance.maintenance import (
    Maintenance,
    MaintenanceCreate,
    MaintenanceUpdate,
)
from green_wind.schema.maintenance.maintenance_action import MaintenanceAction


class CRUDMaintenance(CRUDBase[Maintenance, MaintenanceCreate, MaintenanceUpdate]):
    def create(self, db, *, obj_in) -> Maintenance | None:
        db_model = Maintenance.model_validate(obj_in.model_dump())
        db.add(db_model)
        db.commit()
        db.refresh(db_model)

        db_maintenance_actions = []
        for maintenance_action in obj_in.maintenance_actions:
            maintenance_action = MaintenanceAction(
                maintenance_id=db_model.id, **maintenance_action.model_dump()
            )
            db_maintenance_actions.append(
                crud.maintenance_action.create(db, obj_in=maintenance_action)
            )

        db_model.maintenance_actions = db_maintenance_actions
        return db_model


maintenance = CRUDMaintenance(Maintenance)
