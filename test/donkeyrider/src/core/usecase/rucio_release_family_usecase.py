from src.core.models import LocalRepo
from dependency_injector.wiring import Provide, inject
from src.core.ports.primary.use_case_output_port import UseCaseOutputPort
from src.core.ports.secondary.env_config_output_port import EnvConfigOutputPort
from src.infrastructure.config.ioc import IoCContainer

class RucioReleaseFamilyUseCase:
    """Use case to detect the closest release family to the current HEAD."""
    def __init__(self, local_repo: str, upstream_url: str):
        self.local_repo = local_repo
        self.upstream_url = upstream_url

    @inject
    def execute(self, 
        env_gateway: EnvConfigOutputPort = Provide[IoCContainer.env_gateway],
        presenter: UseCaseOutputPort = Provide[IoCContainer.presenter]
        ):
        
        

    

