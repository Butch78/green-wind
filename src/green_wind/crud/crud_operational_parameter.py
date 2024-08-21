from green_wind.crud.base import CRUDBase

from green_wind.schema.operational_parameters import (
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
