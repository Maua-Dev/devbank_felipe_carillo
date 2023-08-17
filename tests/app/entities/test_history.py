import pytest
from src.app.entities.history import History
from src.app.errors.entity_errors import ParamNotValidated


class Test_History:
    def test_history(self):
        history = History(all_transactions=[])
        assert history.all_transactions == []
        assert history.to_dict() == {
            "all_transactions": []
        }

    def test_history_none(self):
        history = History(all_transactions=None)
        assert history.all_transactions == []
