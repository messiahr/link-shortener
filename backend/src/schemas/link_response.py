from datetime import datetime

from pydantic import BaseModel, HttpUrl


class LinkResponse(BaseModel):
    original_url: HttpUrl
    slug: str
    owner_id: str
    created_at: datetime
