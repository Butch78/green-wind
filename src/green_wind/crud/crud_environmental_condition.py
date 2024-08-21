from green_wind.crud.base import CRUDBase

from green_wind.schema.environmental_conditions import (
    EnvironmentalCondition,
    EnvironmentalConditionsCreate,
    EnvironmentalConditionsUpdate,
)


class CRUDEnvironmentalCondition(
    CRUDBase[
        EnvironmentalCondition,
        EnvironmentalConditionsCreate,
        EnvironmentalConditionsUpdate,
    ]
):
    pass


environmental_condition = CRUDEnvironmentalCondition(EnvironmentalCondition)
