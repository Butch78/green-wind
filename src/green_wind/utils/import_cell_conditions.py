import csv
from datetime import datetime
from sqlmodel import Session

from green_wind.schema.cell_conditions import CellConditionsCreate
from green_wind import crud

def import_cell_conditions(session: Session) -> list[CellConditionsCreate] | None:
    if crud.cell_conditions.get(session, id=1):
        return None

    cell_conditions: list[CellConditionsCreate] = []

    with open(
        "data/processed/processed_cell_conditions.csv",
        newline="\n",
    ) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        for row in reader:
            # column_names = barcode,Ddataset,batch_date,cycle_life,charging_policy,c1,percent,c2
            cell_condition = CellConditionsCreate(
                barcode=row["barcode"],
                dataset=row["dataset"],
                batch_date=datetime.strptime(row["batch_date"], "%d/%m/%Y"),
                cycle_life=int(row["cycle_life"]),
                charging_policy=row["charging_policy"],
                c1=float(row["c1"]),
                percent=int(row["percent"]),
                c2=float(row["c2"]),
            )
            cell_conditions.append(cell_condition)

    crud.cell_conditions.create_multiple(session, obj_in=cell_conditions)

    return cell_conditions
