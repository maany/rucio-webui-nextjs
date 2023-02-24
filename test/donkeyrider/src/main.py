from pathlib import Path
import sys
import click
from src.api.repos import LocalRepo
import os


@click.group()
def cli():
    """Donkey Rider CLI for Rucio WebUI"""
    pass

@cli.group()
def webui():
    """Repository commands"""
    pass

@webui.command()
@click.option("--path", type=click.Path(exists=True), help="Path to the local repository containing the .git repository")
@click.option("--upstream", default="rucio/webui", help="Upstream repository")
@click.option("--upstream-rucio", default="rucio/rucio", help="Upstream Rucio repository")
@click.option("--upstream-containers", default="rucio/containers", help="Upstream containers repository")
@click.option("--github-token", default=os.environ.get("GITHUB_TOKEN"), help="Github Access token")
def init(path: Path, upstream, upstream_rucio, upstream_containers, github_token):
    if path is None:
        sys.exit("A valid path to the local repository is required. Please specify it with the --path option.")
    path = Path(path)
    git_path = path / ".git"
    if not git_path.exists():
        sys.exit(f"Path {path} is not a valid git repository. Please specify a valid path to the local repository with the --path option.")

    if github_token is None:
        sys.exit("A valid Github token is required. Please specify it with the --github-token option or set the GITHUB_TOKEN environment variable.")
    
    print(f"Initializing repository at {path}...")
    webui_local_repo = LocalRepo(path, upstream, github_token)
    click.echo("Repository initialized")
    # click.echo(f"Repository type: {webui_local_repo.head}")

if __name__ == "__main__":
    init(["--path", "../../", "--upstream", "maany/rucio-webui-nextjs"])