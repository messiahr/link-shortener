from dataclasses import dataclass
from datetime import datetime


@dataclass
class Link:
    id: int
    original_url: str
    slug: str
    created_at: datetime
