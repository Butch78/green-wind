from green_wind.crud.base import CRUDBase

from green_wind.schema.energy_throughput import (
    EnergyThroughputCreate,
    EnergyThroughputUpdate,
    EnergyThroughput,
)


class CRUDEnergy_throughput(
    CRUDBase[EnergyThroughput, EnergyThroughputCreate, EnergyThroughputUpdate]
):
    pass


energy_throughput = CRUDEnergy_throughput(EnergyThroughput)
