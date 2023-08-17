import pytest
from src.app.entities.transaction import Transaction
from src.app.enums.TransactionsTypeEnum import TransactionsTypeEnum
from src.app.errors.entity_errors import ParamNotValidated


class Test_Transaction:
    def test_transaction(self):
        transaction = Transaction(type_transactions=TransactionsTypeEnum.deposit, value=100.0, current_balance=100.0)
        assert transaction.type.value == "deposit"
        assert transaction.value == 100
        assert transaction.current_balance == 100
        assert transaction.timestamp is not None
        assert transaction.to_dict() == {
            "type": "deposit",
            "value": 100.0,
            "current_balance": 100.0,
            "timestamp": transaction.timestamp
        }

    def test_transaction_type_none(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(type_transactions=None, value=100.0, current_balance=100.0)

    def test_transaction_invalid_type(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(type_transactions="deposit", value=100.0, current_balance=100.0)

    def test_transaction_invalid_value_none(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(type_transactions=TransactionsTypeEnum.deposit, value=None, current_balance=100.0)

    def test_transaction_invalid_value(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(type_transactions=TransactionsTypeEnum.deposit, value="100.0",
                                      current_balance=100.0)

    def test_transaction_invalid_value_negative(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(type_transactions=TransactionsTypeEnum.deposit, value=-100.0,
                                      current_balance=100.0)

    def test_transaction_invalid_current_balance_none(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(type_transactions=TransactionsTypeEnum.deposit, value=100.0, current_balance=None)

    def test_transaction_invalid_current_balance(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(type_transactions=TransactionsTypeEnum.deposit, value=100.0,
                                      current_balance="100.0")

    def test_transaction_invalid_current_balance_negative(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(type_transactions=TransactionsTypeEnum.deposit, value=100.0,
                                      current_balance=-100.0)

