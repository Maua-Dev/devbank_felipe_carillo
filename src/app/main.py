from typing import Dict

from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments
from .entities.transaction import Transaction
from .enums.TransactionsTypeEnum import TRANSACTION_TYPE

app = FastAPI()

repo_user = Environments.get_user_repo()
repo_transactions = Environments.get_transactions_repo()


@app.get("/")
def get_user() -> Dict:
    user = repo_user.get_user().to_dict()
    return user


@app.post("/deposit", status_code=201)
def create_deposit(request: dict) -> dict:
    if not isinstance(request, dict) or any(not isinstance(value, int) for value in request.values()):
        raise HTTPException(status_code=400, detail="Response must be a dict with int values")

    total_deposit = sum(int(key) * value for key, value in request.items())

    if total_deposit <= 0:
        raise HTTPException(status_code=400, detail="É necessário um valor maior que zero")

    user = repo_user.get_user()
    min_suspect_multiplier = 2
    if user.current_balance * min_suspect_multiplier <= total_deposit:
        raise HTTPException(status_code=403, detail="Depósito suspeito")

    transaction = Transaction(
        type_transactions=TRANSACTION_TYPE.DEPOSIT,
        value=float(total_deposit),
        current_balance=user.current_balance
    )

    response = repo_transactions.create_transaction(transaction)
    repo_user.update_current_balance(response["current_balance"])

    return response


@app.post("/withdraw", status_code=201)
def create_withdraw(request: dict):
    if not isinstance(request, dict) or any(not isinstance(value, int) for value in request.values()):
        raise HTTPException(status_code=400, detail="Invalid input format")

    total_withdrawal = sum(int(key) * value for key, value in request.items())

    if total_withdrawal <= 0:
        raise HTTPException(status_code=400, detail="É necessário um valor maior que zero")

    user = repo_user.get_user()
    if user.current_balance < total_withdrawal:
        raise HTTPException(status_code=403, detail="Saldo insuficiente para transação")

    transaction = Transaction(
        type_transactions=TRANSACTION_TYPE.WITHDRAW,
        value=float(total_withdrawal),
        current_balance=user.current_balance
    )

    response = repo_transactions.create_transaction(transaction)
    repo_user.update_current_balance(response["current_balance"])

    return response


@app.get("/history")
def get_history() -> Dict:
    history = repo_transactions.get_transactions_history()
    return history.to_dict()


handler = Mangum(app, lifespan="off")
