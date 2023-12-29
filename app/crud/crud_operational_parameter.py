from app.crud.base import CRUDBase

from app.schema.operational_parameters import (
    OperationalParameter,
    OperationalParametersCreate,
    OperationalParametersUpdate,
)


class CRUDOperationalParameter(
    CRUDBase[
        OperationalParameter,
        OperationalParametersCreate,
        OperationalParametersUpdate,
    ]
):
    pass


operational_parameter = CRUDOperationalParameter(OperationalParameter)
