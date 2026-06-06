from pydantic import BaseModel, HttpUrl


class LinkRequest(BaseModel):
    original_url: HttpUrl
    slug: str
