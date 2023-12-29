from app.crud.base import CRUDBase

from app.schema.energy_throughput import (
    EnergyThroughputCreate,
    EnergyThroughputUpdate,
    EnergyThroughput,
)


class CRUDEnergy_throughput(
    CRUDBase[EnergyThroughput, EnergyThroughputCreate, EnergyThroughputUpdate]
):
    pass


energy_throughput = CRUDEnergy_throughput(EnergyThroughput)
