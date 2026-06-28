from datetime import datetime

from pydantic import (
    BaseModel,
    ConfigDict,
)


class ApiKeyCreate(BaseModel):

    owner: str


class ApiKeyResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    key: str

    owner: str

    enabled: bool

    created_at: datetime
