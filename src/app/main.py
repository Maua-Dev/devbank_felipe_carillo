from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments

from .errors.entity_errors import ParamNotValidated

app = FastAPI()

repo = Environments.get_user_repo()


@app.get("/")
def get_user():
    user = repo.get_user()
    return user

@app.post("/deposit")
def make_deposit(request: dict):
    try:
        user = repo.get_user()

        return user
    except ParamNotValidated as err:
        raise HTTPException(status_code=400, detail=err.message)


handler = Mangum(app, lifespan="off")
