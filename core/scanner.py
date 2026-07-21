import os

IGNORE = {
    ".git",
    "__pycache__",
    ".idea",
    ".vscode",
    "node_modules"
}


def scan_repo(path):

    result = []

    for root, dirs, files in os.walk(path):

        dirs[:] = [d for d in dirs if d not in IGNORE]

        level = root.replace(path, "").count(os.sep)

        indent = "    " * level

        result.append(f"{indent}{os.path.basename(root)}/")

        for file in files:

            result.append(f"{indent}    {file}")

    return result