from time import time
from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.TransactionsTypeEnum import TransactionsTypeEnum


class Transaction:
    type: TransactionsTypeEnum
    value: float
    current_balance: float
    timestamp: float  # miliseconds

    def __init__(self, type_transactions: TransactionsTypeEnum = None, value: float = None,
                 current_balance: float = None):
        validation_type = self.validate_type(type_transactions)
        if validation_type[0] is False:
            raise ParamNotValidated("type", validation_type[1])
        self.type = type_transactions

        validation_value = self.validate_value(value)
        if validation_value[0] is False:
            raise ParamNotValidated("value", validation_value[1])
        self.value = value

        validation_current_balance = self.validate_current_balance(current_balance)
        if validation_current_balance[0] is False:
            raise ParamNotValidated("current_balance", validation_current_balance[1])
        self.current_balance = current_balance

        timestamp = time() * 1000
        validation_timestamp = self.validate_timestamp(timestamp)
        if validation_timestamp[0] is False:
            raise ParamNotValidated("timestamp", validation_timestamp[1])
        self.timestamp = round(timestamp, 4)

    @staticmethod
    def validate_type(type_transactions: TransactionsTypeEnum) -> Tuple[bool, str]:
        if type_transactions is None:
            return False, "Type is required"
        if type(type_transactions) != TransactionsTypeEnum:
            return False, "Type must be a TransactionsTypeEnum"
        return True, ""

    @staticmethod
    def validate_value(value: float) -> Tuple[bool, str]:
        if value is None:
            return False, "Value is required"
        if type(value) != float:
            return False, "Value must be a float"
        if value < 0:
            return False, "Value must be a positive number"
        return True, ""

    @staticmethod
    def validate_current_balance(current_balance: float) -> Tuple[bool, str]:
        if current_balance is None:
            return False, "Current balance is required"
        if type(current_balance) != float:
            return False, "Current balance must be a float"
        if current_balance < 0:
            return False, "Current balance must be a positive number"
        return True, ""

    @staticmethod
    def validate_timestamp(timestamp: float) -> Tuple[bool, str]:
        if timestamp is None:
            return False, "Timestamp is required"
        if type(timestamp) != float:
            return False, "Timestamp must be a datetime"
        return True, ""

    def to_dict(self) -> dict:
        return {
            "type": self.type.value,
            "value": self.value,
            "current_balance": self.current_balance,
            "timestamp": self.timestamp
        }
