import shutil
import os
from git import Repo

CLONE_DIR = "cloned_repos"


def clone_repo(url):
    repo_name = url.split("/")[-1].replace(".git", "")
    target = os.path.join(CLONE_DIR, repo_name)

    if os.path.exists(target):
        shutil.rmtree(target)

    os.makedirs(CLONE_DIR, exist_ok=True)

    Repo.clone_from(url, target)

    return target