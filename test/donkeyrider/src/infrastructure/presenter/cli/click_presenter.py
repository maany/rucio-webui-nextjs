import click
from src.core.data.use_case_response import UseCaseResponseModel
from src.core.ports.primary.use_case_output_port import UseCaseOutputPort


class ClickPresenter(UseCaseOutputPort):
    def __init__(self, context):
        self.click_context = context

    def success(self, response: UseCaseResponseModel):
        click.echo(response.message)
        click.echo(response.data)

    def error(self, response: UseCaseResponseModel):
        click.echo("ERROR")
        click.echo(response.message)
        click.echo(response.data)

