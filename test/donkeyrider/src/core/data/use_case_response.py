class UseCaseResponseModel:
    @property
    def message(self) -> str:
        return self._message

    @property
    def data(self) -> dict:
        return self._data

    def __init__(self, message: str, data: dict):
        self._message = message
        self._data = data