from green_wind.schema.capacity import Capacity
from green_wind.schema.current import Current
from green_wind.schema.energy_throughput import EnergyThroughput
from green_wind.schema.environmental_conditions import EnvironmentalCondition
from green_wind.schema.operational_parameters import OperationalParameter
from green_wind.schema.temperature import Temperature
from green_wind.schema.voltage import Voltage
from sqlmodel import SQLModel
from green_wind import crud
from typing import Optional
from green_wind.crud.base import CRUDBase

from green_wind.schema.battery_data import (
    BatteryData,
    BatteryDataCreate,
    BatteryDataUpdate,
)


class CRUDBatteryData(CRUDBase[BatteryData, BatteryDataCreate, BatteryDataUpdate]):
    def create_child(self, db, *, obj_in: SQLModel) -> Optional[SQLModel]:
        db.add(obj_in)
        db.commit()
        db.refresh(obj_in)

        return obj_in

    def create(self, db, *, obj_in) -> BatteryData | None:
        db_model = BatteryData.model_validate(obj_in.model_dump())
        db.add(db_model)
        db.commit()
        db.refresh(db_model)

        db_model.voltage = self.create_child(
            db,
            obj_in=Voltage(battery_data_id=db_model.id, **obj_in.voltage.model_dump()),
        )
        db_model.capacity = self.create_child(
            db,
            obj_in=Capacity(
                battery_data_id=db_model.id, **obj_in.capacity.model_dump()
            ),
        )
        db_model.temperature = self.create_child(
            db,
            obj_in=Temperature(
                battery_data_id=db_model.id, **obj_in.temperature.model_dump()
            ),
        )
        db_model.current = self.create_child(
            db,
            obj_in=Current(battery_data_id=db_model.id, **obj_in.current.model_dump()),
        )
        db_model.energy_throughput = self.create_child(
            db,
            obj_in=EnergyThroughput(
                battery_data_id=db_model.id, **obj_in.energy_throughput.model_dump()
            ),
        )
        db_model.environmental_conditions = self.create_child(
            db,
            obj_in=EnvironmentalCondition(
                battery_data_id=db_model.id,
                **obj_in.environmental_conditions.model_dump(),
            ),
        )
        db_model.operational_parameters = self.create_child(
            db,
            obj_in=OperationalParameter(
                battery_data_id=db_model.id,
                **obj_in.operational_parameters.model_dump(),
            ),
        )

        db_model.status = crud.status.create(db, obj_in=obj_in.status)
        db_model.maintenance = crud.maintenance.create(db, obj_in=obj_in.maintenance)

        return db_model

    #
    # capacity = Capacity(obj_in.capacity)
    # voltage = Voltage(obj_in.voltage)
    # temperature = Temperature(obj_in.temperature)
    # current = Current(obj_in.current)
    # status = Status(obj_in.status)
    # energy_throughput = EnergyThroughput(obj_in.energy_throughput)
    # maintenance = Maintenance(obj_in.maintenance)
    # environmental_conditions = EnvironmentalCondition(
    #     obj_in.environmental_conditions
    # )
    # operational_parameters = OperationalParameter(obj_in.operational_parameters)

    # setattr(db_model, "voltage", voltage)
    # setattr(db_model, "capacity", capacity)
    # setattr(db_model, "temperature", temperature)
    # setattr(db_model, "current", current)
    # setattr(db_model, "status", status)
    # setattr(db_model, "energy_throughput", energy_throughput)
    # setattr(db_model, "maintenance", maintenance)
    # setattr(db_model, "environmental_conditions", environmental_conditions)
    # setattr(db_model, "operational_parameters", operational_parameters)

    # print(db_model)
    # db.add(db_model)
    # db.commit()
    # db.refresh(db_model)
    # return db_model


battery_data = CRUDBatteryData(BatteryData)
