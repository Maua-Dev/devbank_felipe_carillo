from abc import ABC, abstractmethod
from typing import List, Dict

from src.app.entities.transaction import Transaction
from src.app.entities.user import User


class IHistoryRepository(ABC):

    @abstractmethod
    def get_history(self) -> Dict[str, List[Transaction]]:
        """
        Returns all transactions in the database
        """
        pass

    @abstractmethod
    def create_transaction(self, transaction: Transaction = None) -> Transaction:
        """
        Returns transaction in the database
        """
        pass


class ITransactionRepository:
    pass
