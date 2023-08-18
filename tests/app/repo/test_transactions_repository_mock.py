import pytest
from src.app.entities.transaction import Transaction
from src.app.repo.transictions_repo.transactions_repository_mock import TransactionsRepositoryMock
from src.app.enums.TransactionsTypeEnum import TRANSACTION_TYPE


class Test_TransactionsRepositoryMock:

    def test_create_transaction_deposit(self):
        repo = TransactionsRepositoryMock()
        transaction = Transaction(type_transactions=TRANSACTION_TYPE.DEPOSIT, value=100.0, current_balance=100.0)
        response = repo.create_transaction(transaction=transaction)
        assert response["current_balance"] == 200.0

    def test_create_transaction_withdraw(self):
        repo = TransactionsRepositoryMock()
        transaction = Transaction(type_transactions=TRANSACTION_TYPE.WITHDRAW, value=100.0, current_balance=100.0)
        response = repo.create_transaction(transaction=transaction)
        assert response["current_balance"] == 0.0

    def test_get_transactions_history(self):
        repo = TransactionsRepositoryMock()
        response = repo.get_transactions_history().to_dict()
        assert response == repo.history.to_dict()


