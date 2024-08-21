from green_wind.crud.base import CRUDBase

from green_wind.schema.status.fault import Fault, FaultCreate, FaultUpdate


class CRUDFault(CRUDBase[Fault, FaultCreate, FaultUpdate]):
    pass


fault = CRUDFault(Fault)
