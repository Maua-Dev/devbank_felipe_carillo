import pytest
from src.app.entities.transaction import Transaction
from src.app.enums.TransactionsTypeEnum import TRANSACTION_TYPE
from src.app.errors.entity_errors import ParamNotValidated


class Test_Transaction:
    def test_transaction(self):
        transaction = Transaction(type_transactions=TRANSACTION_TYPE.DEPOSIT, value=100.0, current_balance=100.0)
        assert transaction.type == TRANSACTION_TYPE.DEPOSIT
        assert transaction.value == 100
        assert transaction.current_balance == 100
        assert transaction.timestamp is not None

    def test_transaction_type_none(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(type_transactions=None, value=100.0, current_balance=100.0)

    def test_transaction_invalid_type(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(type_transactions="deposit", value=100.0, current_balance=100.0)

    def test_transaction_invalid_value_none(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(type_transactions=TRANSACTION_TYPE.DEPOSIT, value=None, current_balance=100.0)

    def test_transaction_invalid_value(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(type_transactions=TRANSACTION_TYPE.DEPOSIT, value="100.0",
                                      current_balance=100.0)

    def test_transaction_invalid_value_negative(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(type_transactions=TRANSACTION_TYPE.DEPOSIT, value=-100.0,
                                      current_balance=100.0)

    def test_transaction_invalid_current_balance_none(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(type_transactions=TRANSACTION_TYPE.DEPOSIT, value=100.0, current_balance=None)

    def test_transaction_invalid_current_balance(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(type_transactions=TRANSACTION_TYPE.DEPOSIT, value=100.0,
                                      current_balance="100.0")

    def test_transaction_invalid_current_balance_negative(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(type_transactions=TRANSACTION_TYPE.DEPOSIT, value=100.0,
                                      current_balance=-100.0)

