import os

TARGET_FILES = [
    "README.md",
    "requirements.txt",
    "Dockerfile",
    "docker-compose.yml",
    "pyproject.toml",
]


def load_files(repo):

    data = {}

    for root, dirs, files in os.walk(repo):

        for file in files:

            if file in TARGET_FILES:

                path = os.path.join(root, file)

                try:

                    with open(path, "r", encoding="utf8") as f:

                        data[file] = f.read()

                except:

                    pass

    return data