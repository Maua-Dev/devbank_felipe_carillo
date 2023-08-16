from typing import List
from ..entities.transaction import Transaction


class History:
    all_transactions: List[Transaction]

    def __init__(self, all_transactions: List[Transaction] = None):
        self.all_transactions = all_transactions

