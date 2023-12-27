from fastapi import APIRouter, HTTPException, Query, Depends
from sqlmodel import Session

from app.utils.deps import get_session
from app import crud
from app.schema.battery_data import (
    BatteryDataCreate,
    BatteryDataRead,
    BatteryDataUpdate,
    BatteryDataReadOut,
)

router = APIRouter()


@router.get("/", response_model=list[BatteryDataRead])
def read_battery_data(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1),
    session: Session = Depends(get_session),
):
    return crud.battery_data.get_multi(session, skip=skip, limit=limit)


@router.get("/{id}", response_model=BatteryDataReadOut)
def read_battery_data_by_id(
    *,
    id: int,
    session: Session = Depends(get_session),
):
    battery_data = crud.battery_data.get(session, id=id)
    if not battery_data:
        raise HTTPException(status_code=404, detail="Battery data not found")
    return battery_data


@router.post("/", response_model=BatteryDataRead)
def create_battery_data(
    *,
    battery_data_in: BatteryDataCreate,
    session: Session = Depends(get_session),
):
    battery_data = crud.battery_data.create(session, obj_in=battery_data_in)
    return battery_data


@router.put("/{id}", response_model=BatteryDataReadOut)
def update_battery_data(
    *,
    id: int,
    battery_data_in: BatteryDataUpdate,
    session: Session = Depends(get_session),
):
    battery_data = crud.battery_data.get(session, id=id)
    if not battery_data:
        raise HTTPException(status_code=404, detail="Battery data not found")
    battery_data = crud.battery_data.update(
        session, db_obj=battery_data, obj_in=battery_data_in
    )
    return battery_data
