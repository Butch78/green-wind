from app.crud.base import CRUDBase

from app.schema.status.fault import Fault, FaultCreate, FaultUpdate


class CRUDFault(CRUDBase[Fault, FaultCreate, FaultUpdate]):
    pass


fault = CRUDFault(Fault)
