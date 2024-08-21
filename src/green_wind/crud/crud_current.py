from green_wind.crud.base import CRUDBase

from green_wind.schema.current import Current, CurrentCreate, CurrentUpdate


class CRUDCurrent(CRUDBase[Current, CurrentCreate, CurrentUpdate]):
    pass


current = CRUDCurrent(Current)
