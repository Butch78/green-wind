from app.crud.base import CRUDBase

from app.schema.current import Current, CurrentCreate, CurrentUpdate


class CRUDCurrent(CRUDBase[Current, CurrentCreate, CurrentUpdate]):
    pass


current = CRUDCurrent(Current)
