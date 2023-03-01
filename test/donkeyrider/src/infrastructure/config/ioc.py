from dependency_injector import containers, providers

from src.infrastructure.gateway.env_gateway import EnvGateway

class IoCContainer(containers.DeclarativeContainer):
    env_gateway = providers.Singleton(EnvGateway)

    presenter = providers.Factory()