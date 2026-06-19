from pydantic import BaseModel


class UpstreamService(BaseModel):

    name: str

    url: str
