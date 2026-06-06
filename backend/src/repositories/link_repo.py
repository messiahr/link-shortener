import abc
from typing import override

from sqlalchemy import select
from sqlalchemy.orm import Session

from ..database.models import LinkORM
from ..domain.link import Link
from .link_mapper import to_domain


class AbstractLinkRepo(abc.ABC):
    @abc.abstractmethod
    def get_link(self, slug: str) -> Link | None:
        pass

    @abc.abstractmethod
    def save_link(self, original_url: str, slug: str, id: str) -> Link:
        pass


class LinkRepo(AbstractLinkRepo):
    def __init__(self, db: Session):
        self.db: Session = db

    @override
    def get_link(self, slug: str) -> Link | None:
        orm_link = self.db.scalar(select(LinkORM).where(LinkORM.slug == slug))

        if orm_link is None:
            raise ValueError(f"Link with slug {slug} not found")

        return to_domain(orm_link)

    @override
    def save_link(self, original_url: str, slug: str, id: str) -> Link:
        orm_link = LinkORM(
            original_url=original_url,
            slug=slug,
            owner_id=id,
        )

        self.db.add(orm_link)
        self.db.commit()
        self.db.refresh(orm_link)

        return to_domain(orm_link)
