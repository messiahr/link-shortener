from ..database.models import LinkORM
from ..domain.link import Link


def to_domain(link: LinkORM) -> Link:
    return Link(
        id=link.id,
        original_url=str(link.original_url),
        slug=link.slug,
        created_at=link.created_at,
        owner_id=link.owner_id,
    )
