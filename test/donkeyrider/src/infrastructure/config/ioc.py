from dependency_injector import containers, providers
from src.core.usecase.rucio_release_family_usecase import RucioReleaseFamilyUseCase
from src.infrastructure.controller.webui_repo_controller import WebUIRepoController

from src.infrastructure.gateway.env_gateway import EnvGateway
from src.infrastructure.presenter.cli.click_presenter import ClickPresenter

class IoCContainer(containers.DeclarativeContainer):
    env_gateway = providers.Singleton(EnvGateway)

    presenter = providers.Factory(
        ClickPresenter,
    )

    use_case_rucio_release_family = providers.Factory(
        RucioReleaseFamilyUseCase,
        env_gateway=env_gateway,
        presenter=presenter,
    )

    webui_repo_controller = providers.Singleton(
        WebUIRepoController,
        rucio_release_family_use_case=use_case_rucio_release_family,
    )