from fastapi import APIRouter, Query, Depends
from sqlmodel import Session

from app.utils.deps import get_session
from app import crud

#  TODO Create endpoint for posting battery data

