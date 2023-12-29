from app.crud.base import CRUDBase

from app.schema.environmental_conditions import (
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
