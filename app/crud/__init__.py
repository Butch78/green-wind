#  Train data Crud
from app.crud.crud_cell_conditions import cell_conditions
from app.crud.crud_cell_training_data import cell_training_data


# Battery data Crud
from app.crud.crud_battery_data import battery_data
from app.crud.crud_voltage import voltage
from app.crud.crud_capacity import capacity
from app.crud.crud_current import current
from app.crud.crud_energy_throughput import energy_throughput
from app.crud.crud_environmental_condition import environmental_condition
from app.crud.crud_operational_parameter import operational_parameter
from app.crud.crud_maintenance import maintenance
from app.crud.crud_maintenance_action import maintenance_action
from app.crud.crud_status import status
from app.crud.crud_fault import fault
from app.crud.crud_temperature import temperature

temperature = temperature
maintenance_action = maintenance_action
fault = fault
maintenance = maintenance
status = status


operational_parameter = operational_parameter

cell_conditions = cell_conditions
cell_training_data = cell_training_data


energy_throughput = energy_throughput
environmental_condition = environmental_condition

voltage = voltage
battery_data = battery_data
capacity = capacity

current = current
