from typing import Dict
from ...entities.history import History
from ...entities.transaction import Transaction
from ...enums.TransactionsTypeEnum import TransactionsTypeEnum

from .transactions_repository_interface import ITransactionsRepository


class TransactionsRepositoryMock(ITransactionsRepository):
    history: History
    transaction: Transaction

    def __init__(self):
        self.history = History()

    def create_transaction(self, transaction: Transaction = None) -> Dict[str, float]:
        if transaction.type == TransactionsTypeEnum.deposit:
            transaction.current_balance = transaction.current_balance + transaction.value
        elif transaction.type == TransactionsTypeEnum.withdraw:
            transaction.current_balance = transaction.current_balance - transaction.value

        transaction = Transaction(
            type_transactions=transaction.type,
            value=transaction.value,
            current_balance=transaction.current_balance
        )

        self.history.all_transactions.append(transaction)
        return {"current_balance": transaction.current_balance, "timestamp": transaction.timestamp}

    def get_transactions_history(self):
        return self.history
