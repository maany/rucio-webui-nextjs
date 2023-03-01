from abc import ABC, abstractmethod


class EnvConfigOutputPort(ABC):
    @abstractmethod
    def get(self, name: str) -> str:
        """_summary_

        Args:
            name (str): the name of the environment or configuration variable to fetch

        Returns:
            str: the value of the environment or configuration variable
        """
        pass