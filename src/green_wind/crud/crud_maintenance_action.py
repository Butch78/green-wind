from green_wind.crud.base import CRUDBase
from green_wind.schema.maintenance.maintenance_action import (
    MaintenanceActionCreate,
    MaintenanceActionUpdate,
    MaintenanceAction,
)


class CRUDMaintenanceAction(
    CRUDBase[MaintenanceAction, MaintenanceActionCreate, MaintenanceActionUpdate]
):
    pass


maintenance_action = CRUDMaintenanceAction(MaintenanceAction)
