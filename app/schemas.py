from datetime import datetime

from pydantic import BaseModel, ConfigDict


class JobCreate(BaseModel):
    task_type: str
    payload: dict = {}


class JobRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    task_type: str
    payload: dict
    status: str
    result: str | None
    attempts: int
    created_at: datetime
    updated_at: datetime
