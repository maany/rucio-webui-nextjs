from threading import local
from src.core.usecase.rucio_release_family_usecase import RucioReleaseFamilyUseCase


class WebUIRepoController:
    """_summary_ Provides functions to interact with the WebUI testing use cases
    """
    def __init__(self, rucio_release_family_use_case):
        self.rucio_release_family_use_case: RucioReleaseFamilyUseCase = rucio_release_family_use_case
    
    def handle(self, local_repo: str, upstream_url: str):
        self.rucio_release_family_use_case.execute(local_repo, upstream_url)

    