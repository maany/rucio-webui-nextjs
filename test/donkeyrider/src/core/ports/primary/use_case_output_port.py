from abc import ABC, abstractmethod


class UseCaseOutputPort(ABC):
    """Output port for the RucioReleaseFamilyUseCase."""
    @abstractmethod
    def success(self, release_family: str) -> None:
        """Present the release family to the user."""
        raise NotImplementedError

    def error(self, message: str) -> None:
        """Present an error message to the user."""
        raise NotImplementedError