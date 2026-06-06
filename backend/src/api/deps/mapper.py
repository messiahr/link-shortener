from pydantic import HttpUrl

from ...domain.link import Link
from ...schemas.link_response import LinkResponse


def to_link_response(link: Link) -> LinkResponse:
    return LinkResponse(
        original_url=HttpUrl(link.original_url),
        slug=link.slug,
        owner_id=link.owner_id,
        created_at=link.created_at,
    )
