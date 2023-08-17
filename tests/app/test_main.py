from fastapi.exceptions import HTTPException
import pytest
from time import time
from src.app.main import get_user, create_deposit, create_withdraw, get_history
from src.app.repo.user_repo.user_repository_mock import UserRepositoryMock
from src.app.repo.history_transictions_repo.transactions_repository_mock import TransactionsRepositoryMock


class Test_Main:
    def test_get_user(self):
        repo = UserRepositoryMock()
        response = get_user()
        assert response == repo.user.to_dict()

    def test_get_history(self):
        repo = TransactionsRepositoryMock()
        response = get_history()
        assert response == repo.history.to_dict()

    def test_create_deposit(self):
        repo = TransactionsRepositoryMock()
        body = {
            "2": 1
        }
        response = create_deposit(request=body)
        assert response == {
            "current_balance": 1002.0,
            "timestamp": time() * 1000
        }

    def test_create_deposit_invalid_input(self):
        repo = TransactionsRepositoryMock()
        body = "200"
        with pytest.raises(HTTPException):
            response = create_deposit(request=body)

    def test_create_deposit_zero(self):
        repo = TransactionsRepositoryMock()
        body = {
            "0": 1
        }
        with pytest.raises(HTTPException):
            response = create_deposit(request=body)

    def test_create_deposit_suspicious(self):
        repo = TransactionsRepositoryMock()
        body = {
            "200": 12
        }
        with pytest.raises(HTTPException):
            response = create_deposit(request=body)

    def test_create_withdraw(self):
        body = {
            "2": 1
        }
        response = create_withdraw(body)
        assert response == {
            "current_balance": 1000,
            "timestamp": time() * 1000
        }

    def test_create_withdraw_invalid_input(self):
        repo = TransactionsRepositoryMock()
        body = "200"
        with pytest.raises(HTTPException):
            response = create_withdraw(request=body)

    def test_create_withdraw_zero(self):
        repo = TransactionsRepositoryMock()
        body = {
            "0": 1
        }
        with pytest.raises(HTTPException):
            response = create_withdraw(request=body)

    def test_create_withdraw_insufficient_funds(self):
        repo = TransactionsRepositoryMock()
        body = {
            "200": 12
        }
        with pytest.raises(HTTPException):
            response = create_withdraw(request=body)
