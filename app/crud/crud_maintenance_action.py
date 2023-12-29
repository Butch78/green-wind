from app.crud.base import CRUDBase
from app.schema.maintenance.maintenance_action import (
    MaintenanceActionCreate,
    MaintenanceActionUpdate,
    MaintenanceAction,
)


class CRUDMaintenanceAction(
    CRUDBase[MaintenanceAction, MaintenanceActionCreate, MaintenanceActionUpdate]
):
    pass


maintenance_action = CRUDMaintenanceAction(MaintenanceAction)
