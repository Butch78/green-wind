from polyfactory.factories.pydantic_factory import ModelFactory
from polyfactory import Use
from app.schema.battery_data import BatteryDataCreate
from app import crud
from sqlmodel import Session


class BatteryDataFactory(ModelFactory[BatteryDataCreate]):
    manufacturer = Use(
        ModelFactory.__random__.choice, ["GreenPowerTech", "Siemens", "Tesla"]
    )
    model = Use(ModelFactory.__random__.choice, ["GPT-3", "Siemens-1", "Tesla-1"])
    current_capacity = Use(
        ModelFactory.__random__.choice, ["4000 kWh", "5000 kWh", "6000 kWh"]
    )
    design_capacity = Use(ModelFactory.__random__.choice, ["6000 kWh"])
    remaining_capacity = Use(
        ModelFactory.__random__.choice, ["4000 kWh", "5000 kWh", "6000 kWh"]
    )
    terminal_voltage = Use(ModelFactory.__random__.choice, ["480 V", "500 V", "600 V"])
    operating_voltage = Use(ModelFactory.__random__.choice, ["480 V", "500 V", "600 V"])
    charging_voltage = Use(ModelFactory.__random__.choice, ["480 V", "500 V", "600 V"])
    internal_temperature = Use(ModelFactory.__random__.choice, ["20 C", "25 C", "30 C"])
    external_temperature = Use(ModelFactory.__random__.choice, ["20 C", "25 C", "30 C"])
    operating_temperature_range = Use(
        ModelFactory.__random__.choice, ["20-40°C", "20-40°C"]
    )
    charging_current = Use(ModelFactory.__random__.choice, ["100 A", "200 A", "300 A"])
    discharging_current = Use(
        ModelFactory.__random__.choice, ["100 A", "200 A", "300 A"]
    )
    operating_current_range = Use(
        ModelFactory.__random__.choice, ["100 A", "200 A", "300 A"]
    )
    state_of_charge = Use(ModelFactory.__random__.choice, ["100%", "90%", "80%"])
    health_status = Use(ModelFactory.__random__.choice, ["Good", "Average", "Bad"])
    operation_status = Use(ModelFactory.__random__.choice, ["Active", "Inactive"])
    fault_description = Use(
        ModelFactory.__random__.choice,
        ["Overtemperature warning", "High voltage warning", "Low voltage warning"],
    )
    total_energy_delivered = Use(
        ModelFactory.__random__.choice, ["1000 kWh", "2000 kWh", "3000 kWh"]
    )
    total_energy_charged = Use(
        ModelFactory.__random__.choice, ["1000 kWh", "2000 kWh", "3000 kWh"]
    )
    action_description = Use(
        ModelFactory.__random__.choice,
        ["Replace cooling fan", "Replace battery", "Replace battery management system"],
    )
    ambient_temperature = Use(ModelFactory.__random__.choice, ["20 C", "25 C", "30 C"])
    humidity = Use(ModelFactory.__random__.choice, ["50%", "60%", "70%"])
    altitude = Use(ModelFactory.__random__.choice, ["0 m", "100 m", "200 m"])
    charge_cycles = Use(ModelFactory.__random__.choice, ["100", "200", "300"])
    discharge_cycles = Use(ModelFactory.__random__.choice, ["100", "200", "300"])
    max_continuous_discharge_rate = Use(
        ModelFactory.__random__.choice, ["100 A", "200 A", "300 A"]
    )
    max_continuous_charge_rate = Use(
        ModelFactory.__random__.choice, ["100 A", "200 A", "300 A"]
    )


def create_battery_data(session: Session):
    for _ in range(100):
        crud.battery_data.create(session, obj_in=BatteryDataFactory.build())
