from fastapi import APIRouter, HTTPException, Query, Depends
from sqlmodel import Session

from green_wind.utils.deps import get_session
from green_wind.schema.battery_data import (
    BatteryDataCreate,
    BatteryDataRead,
    BatteryDataReadOut,
)
from green_wind import crud

router = APIRouter()


@router.get("", response_model=list[BatteryDataReadOut])
def read_battery_data(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1),
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


@router.post("", response_model=BatteryDataRead)
def create_battery_data(
    *,
    battery_data_in: BatteryDataCreate,
    session: Session = Depends(get_session),
):
    battery_data = crud.battery_data.create(session, obj_in=battery_data_in)
    return battery_data
