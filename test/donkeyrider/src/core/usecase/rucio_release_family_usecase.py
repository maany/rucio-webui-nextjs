from src.core.data.use_case_response import UseCaseResponseModel
from src.core.models import LocalRepo
from dependency_injector.wiring import Provide, inject
from src.core.ports.primary.use_case_output_port import UseCaseOutputPort
from src.core.ports.secondary.env_config_output_port import EnvConfigOutputPort


class RucioReleaseFamilyUseCase:
    """Use case to detect the closest release family to the current HEAD."""
    
    def __init__(self, env_gateway: EnvConfigOutputPort, presenter: UseCaseOutputPort):
        self.env_gateway = env_gateway
        self.presenter = presenter

    def execute(self, local_repo: str, upstream_url: str): 
        self.env_gateway.get("GITHUB_TOKEN")
        self.presenter.success(
            UseCaseResponseModel(
                message="Repository initialized",
                data={
                    "local_repo": local_repo,
                    "upstream_url": upstream_url,
                }
            )
        )
        


