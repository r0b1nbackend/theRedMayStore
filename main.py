from beanie import init_beanie
from fastapi import FastAPI
from fastapi_users import fastapi_users, FastAPIUsers
from auth.database import User
from auth.manager import get_user_manager
from auth.schemas import UserRead,UserCreate
from auth.auth import auth_backend
from router.books import book_router
app = FastAPI()


@app.get("/")
def hello():
    return {
        "message":"The Red May(TRM) - is a site with many books of various political contrasts,"
                  "starting from the left-radical and, as far as the law allows, "
                  "from the right-wing political positions."
    }


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(book_router,prefix="/book")


