from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments
from .entities.transaction import Transaction
from .enums.TransactionsTypeEnum import TransactionsTypeEnum
from .errors.entity_errors import ParamNotValidated

app = FastAPI()

repoUser, repoTransactions = Environments.get_repos()


@app.get("/")
def get_user():
    user = repoUser.get_user()
    return user


@app.post("/deposit", status_code=201)
def create_deposit(request: dict):
    value = sum([int(key) * value for key, value in request.items()])
    if value <= 0:
        raise ParamNotValidated("Value must be greater than zero")
    user = repoUser.get_user()
    if user.current_balance * 2 <= value:
        raise HTTPException(status_code=403, detail="Depósito suspeito")
    transaction = Transaction(
        type_transactions=TransactionsTypeEnum["deposit"],
        value=float(value),
        current_balance=user.current_balance
    )
    response = repoTransactions.create_transaction(transaction)
    repoUser.update_current_balance(response["current_balance"])
    return response


@app.post("/withdraw", status_code=201)
def create_withdraw(request: dict):
    value = sum([int(key) * value for key, value in request.items()])
    if value <= 0:
        raise ParamNotValidated("Value must be greater than zero")
    user = repoUser.get_user()
    if user.current_balance < value:
        raise HTTPException(status_code=403, detail="Saldo insuficiente para transação")
    transaction = Transaction(
        type_transactions=TransactionsTypeEnum["withdraw"],
        value=float(value),
        current_balance=user.current_balance
    )
    response = repoTransactions.create_transaction(transaction)
    repoUser.update_current_balance(response["current_balance"])
    return response


@app.get("/history")
def get_history():
    history = repoTransactions.get_history()
    return history


handler = Mangum(app, lifespan="off")
