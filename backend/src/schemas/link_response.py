from datetime import datetime

from pydantic import BaseModel, HttpUrl


class LinkResponse(BaseModel):
    original_url: HttpUrl
    slug: str
    id: int
    created_at: datetime
