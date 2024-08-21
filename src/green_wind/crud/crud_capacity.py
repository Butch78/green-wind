from green_wind.crud.base import CRUDBase

from green_wind.schema.capacity import Capacity, CapacityCreate, CapacityUpdate


class CRUDCapacity(CRUDBase[Capacity, CapacityCreate, CapacityUpdate]):
    pass


capacity = CRUDCapacity(Capacity)
