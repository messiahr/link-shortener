import os
from typing import Annotated

import requests
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from ...schemas.user import User

security = HTTPBearer()

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_PUBLISHABLE_KEY = os.environ["SUPABASE_PUBLISHABLE_KEY"]

BearerToken = Annotated[HTTPAuthorizationCredentials, Depends(security)]


def get_current_user(credentials: BearerToken) -> User:
    token = credentials.credentials

    res = requests.get(
        f"{SUPABASE_URL}/auth/v1/user",
        headers={
            "Authorization": f"Bearer {token}",
            "apikey": SUPABASE_PUBLISHABLE_KEY,
        },
    )

    if res.status_code != 200:
        raise HTTPException(status_code=401, detail="Invalid authentication token")

    return User.model_validate(res.json())


UserDep = Annotated[User, Depends(get_current_user)]
