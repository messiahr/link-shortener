import abc

from sqlalchemy import select

from ..database.models import LinkORM
from ..domain.link import Link


class AbstractLinkRepo(abc.ABC):
    @abc.abstractmethod
    def get_link(self, slug: str) -> Link:
        pass

    @abc.abstractmethod
    def save_link(self, link: str, slug: str) -> Link:
        pass


class LinkRepo(AbstractLinkRepo):
    def __init__(self, db):
        self.db = db

    def get_link(self, slug: str) -> Link:
        statement = select(LinkORM).where(LinkORM.slug == slug)

        result = self.db.execute(statement)

        orm_link = result.scalar_one_or_none()

        if orm_link is None:
            raise ValueError(f"Link with slug {slug} not found")

        return Link(
            id=orm_link.id,
            original_url=orm_link.original_url,
            slug=orm_link.slug,
            created_at=orm_link.created_at,
        )

    def save_link(self, link: str, slug: str) -> Link:
        orm_link = LinkORM(
            original_url=link,
            slug=slug,
        )
        self.db.add(orm_link)
        self.db.commit()
        self.db.refresh(orm_link)
        return Link(
            id=orm_link.id,
            original_url=orm_link.original_url,
            slug=orm_link.slug,
            created_at=orm_link.created_at,
        )
