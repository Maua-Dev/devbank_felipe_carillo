import pytest
from src.app.entities.user import User
from src.app.errors.entity_errors import ParamNotValidated


class Test_User:
    def test_user(self):
        user = User(name="Vitor Soller", agency="0000", account="00000-0", current_balance=1000.0)
        assert user.name == "Vitor Soller"
        assert user.agency == "0000"
        assert user.account == "00000-0"
        assert user.current_balance == 1000.0
        assert user.to_dict() == {
            "name": "Vitor Soller",
            "agency": "0000",
            "account": "00000-0",
            "current_balance": 1000.0
        }

    def test_user_name_none(self):
        with pytest.raises(ParamNotValidated):
            user = User(name=None, agency="0000", account="00000-0", current_balance=1000.0)

    def test_user_name_not_string(self):
        with pytest.raises(ParamNotValidated):
            user = User(name=1, agency="0000", account="00000-0", current_balance=1000.0)

    def test_user_name_less_than_3(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Vi", agency="0000", account="00000-0", current_balance=1000.0)

    def test_user_agency_none(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Vitor Soller", agency=None, account="00000-0", current_balance=1000.0)

    def test_user_agency_not_string(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Vitor Soller", agency=1, account="00000-0", current_balance=1000.0)

    def test_user_agency_not_4_digits(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Vitor Soller", agency="000", account="00000-0", current_balance=1000.0)

    def test_user_account_none(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Vitor Soller", agency="0000", account=None, current_balance=1000.0)

    def test_user_account_not_string(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Vitor Soller", agency="0000", account=1, current_balance=1000.0)

    def test_user_account_not_7_digits(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Vitor Soller", agency="0000", account="000000-0", current_balance=1000.0)

    def test_user_account_not_in_format(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Vitor Soller", agency="0000", account="0000000", current_balance=1000.0)

    def test_user_current_balance_none(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Vitor Soller", agency="0000", account="00000-0", current_balance=None)

    def test_user_current_balance_not_float(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Vitor Soller", agency="0000", account="00000-0", current_balance=1)

    def test_user_current_balance_not_positive(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Vitor Soller", agency="0000", account="00000-0", current_balance=-1)
