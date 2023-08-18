from enum import Enum
import os

from .errors.environment_errors import EnvironmentNotFound
from .repo.transictions_repo.transactions_repository_mock import TransactionsRepositoryMock
from .repo.user_repo.user_repository_mock import UserRepositoryMock


class STAGE(Enum):
    DOTENV = "DOTENV"
    DEV = "DEV"
    PROD = "PROD"
    TEST = "TEST"


def _configure_local():
    from dotenv import load_dotenv
    load_dotenv()
    os.environ["STAGE"] = os.environ.get("STAGE") or STAGE.TEST.value


class Environments:
    """
    Defines the environment variables for the application. You should not instantiate this class directly. Please use Environments.get_envs() method instead.

    Usage:

    """
    stage: STAGE

    def load_envs(self):
        if "STAGE" not in os.environ or os.environ["STAGE"] == STAGE.DOTENV.value:
            _configure_local()

        self.stage = STAGE[os.environ.get("STAGE")]

    @staticmethod
    def get_transactions_repo() -> TransactionsRepositoryMock:
        if Environments.get_envs().stage == STAGE.TEST:
            from .repo.transictions_repo.transactions_repository_mock import TransactionsRepositoryMock
            return TransactionsRepositoryMock()
        else:
            raise EnvironmentNotFound("STAGE")

    @staticmethod
    def get_user_repo() -> UserRepositoryMock:
        if Environments.get_envs().stage == STAGE.TEST:
            from .repo.user_repo.user_repository_mock import UserRepositoryMock
            return UserRepositoryMock()
        else:
            raise EnvironmentNotFound("STAGE")

    @staticmethod
    def get_envs() -> "Environments":
        """
        Returns the Environments object. This method should be used to get the Environments object instead of instantiating it directly.
        :return: Environments (stage={self.stage})

        """
        envs = Environments()
        envs.load_envs()
        return envs

    def __repr__(self):
        return self.__dict__
