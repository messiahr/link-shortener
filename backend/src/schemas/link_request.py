from pydantic import BaseModel


class LinkRequest(BaseModel):
    original_url: str
    slug: str
