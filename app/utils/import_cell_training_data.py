import csv, os
from concurrent.futures import ThreadPoolExecutor
from sqlmodel import Session

from app.schema.cell_training_data import CellDataTrainingCreate
from app import crud


def read_csv_file(file_name: str) -> list[CellDataTrainingCreate]:
    cell_training_data: list[CellDataTrainingCreate] = []

    folder_name = file_name.split("/")[2]

    with open(
        file_name,
        newline="\n",
    ) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            # column_names = folder_name,cell_cycle,cell_voltage,static_cell_voltage
            cell_data_training = CellDataTrainingCreate(
                folder_name=folder_name,
                x_train=int(row[0]),
                y_train=float(row[1]),
                static_cell_voltage=float(row[2]),
            )
            cell_training_data.append(cell_data_training)

    return cell_training_data


def import_cell_training_data(
    session: Session,
) -> list[CellDataTrainingCreate] | None:
    if crud.cell_training_data.get(session, id=1):
        return None

    # folder of files to import
    csv_folders = [
        "data/raw/test1",
        "data/raw/test2",
        "data/raw/test3",
        "data/raw/train",
    ]

    csv_files = []

    for csv_folder in csv_folders:
        csv_files.extend(
            [
                f"{csv_folder}/" + file_name
                for file_name in os.listdir(csv_folder)
                if file_name.endswith(".csv")
            ]
        )

    with ThreadPoolExecutor() as executor:
        results = executor.map(read_csv_file, csv_files)

    cell_training_data = [item for sublist in results for item in sublist]

    crud.cell_training_data.create_multiple(session, obj_in=cell_training_data)

    return cell_training_data
