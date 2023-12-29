from sqlmodel import SQLModel
from typing import Optional
from app.crud.base import CRUDBase

from app.schema.battery_data import BatteryData, BatteryDataCreate, BatteryDataUpdate


class CRUDBatteryData(CRUDBase[BatteryData, BatteryDataCreate, BatteryDataUpdate]):
    def create_child(
        self, db, *, battery_data_id, obj_in, model: SQLModel
    ) -> Optional[SQLModel]:
        db_model = model.model_validate(
            obj_in.model_dump(), battery_data_id=battery_data_id
        )
        db.add(db_model)
        db.commit()
        db.refresh(db_model)

        return db_model

    def create(self, db, *, obj_in) -> BatteryData | None:
        db_model = BatteryData.model_validate(obj_in.model_dump())
        db.add(db_model)
        db.commit()
        db.refresh(db_model)

        # Loop through the fields of BatteryDataCreate
        for field_name, field_type in BatteryDataCreate.__annotations__.items():
            # If the field is a child model and it exists in obj_in
            if field_type.__origin__ is SQLModel and hasattr(obj_in, field_name):
                # Create the child model
                child_obj_in = getattr(obj_in, field_name)
                child_model = field_type.__args__[0]
                child_db_model = self.create_child(
                    db,
                    battery_data_id=db_model.id,
                    obj_in=child_obj_in,
                    model=child_model,
                )
                # Set the child model in db_model
                setattr(db_model, field_name, child_db_model)

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
