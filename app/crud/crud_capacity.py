from app.crud.base import CRUDBase

from app.schema.capacity import Capacity, CapacityCreate, CapacityUpdate


class CRUDCapacity(CRUDBase[Capacity, CapacityCreate, CapacityUpdate]):
    pass


capacity = CRUDCapacity(Capacity)
