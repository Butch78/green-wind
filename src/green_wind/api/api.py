from fastapi import APIRouter

from green_wind.api.api_v1.battery_data import router as battery_data_router

api_router = APIRouter()

api_router.include_router(
    battery_data_router, prefix="/battery_data", tags=["battery_data"]
)
