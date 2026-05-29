from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from src.schemas.link_request import LinkRequest

from .database.db import Base, SessionLocal, engine
from .repositories.link_repo import LinkRepo

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/links")
def create_link(link_request: LinkRequest, db: Session = Depends(get_db)):
    repo = LinkRepo(db)

    link = repo.save_link(link_request.original_url, link_request.slug)

    return {
        "original_url": link.original_url,
        "slug": link.slug,
    }


@app.get("/{slug}")
def get_link(slug: str, db: Session = Depends(get_db)):
    repo = LinkRepo(db)

    link = repo.get_link(slug)

    if link is None:
        raise ValueError(f"Link with slug {slug} not found")

    return RedirectResponse(link.original_url)
