from pathlib import Path
from git import Repo
import os

class WebUI:
    @property
    def path(self):
        return 'webui'
    

# Get the path to the webui source code

# Get the git ref for the webui

# If ref is master, then rucio_tag is latest tag in the latest release line

# If ref is not master, then we need to find what release line of rucio webui the current ref belongs to

# For the current ref, rucio_tag is the latest tag in the same release line


# Get the repo owner from the environment
owner = os.getenv('GITHUB_OWNER')
if not owner:
    pass

# Clone the rucio/rucio repo
repo = Repo.clone_from('rucio/rucio', 'rucio')

# Get the latest tag
latest_tag = repo.tags[-1]


if __name__  == "__main__":
    