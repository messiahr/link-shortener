from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from ..database.db import Base, engine
from ..repositories.link_repo import LinkRepo
from ..schemas.link_request import LinkRequest
from ..schemas.link_response import LinkResponse
from .deps.auth import UserDep
from .deps.db import DBSession

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/links", response_model=LinkResponse)
def create_link(
    link_request: LinkRequest,
    user: UserDep,
    db: DBSession,
):
    repo = LinkRepo(db)

    link = repo.save_link(
        original_url=str(link_request.original_url),
        slug=link_request.slug,
        user_id=user.id,
    )

    return LinkResponse.model_validate(link)


@app.get("/links", response_model=list[LinkResponse])
def get_links_by_user(
    user: UserDep,
    db: DBSession,
):
    repo = LinkRepo(db)

    return [
        LinkResponse.model_validate(link) for link in repo.get_links_by_user(user.id)
    ]


@app.get("/{slug}")
def get_link(slug: str, db: DBSession):
    repo = LinkRepo(db)

    link = repo.get_link(slug)

    if link is None:
        raise ValueError(f"Link with slug {slug} not found")

    return RedirectResponse(link.original_url)
