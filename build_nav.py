# Builds the nav for an mkdocs site. Usually you would want to leave the nav
# empty and have mkdocs build it for you, but defining the nav is necessary
# if you use the navigation.tabs feature.
#
# Everything is sorted in alphabetical order with all files coming
#   before all directories in the same depth level.
# You must pre-define the order of your tabs in the TAB_ORDER list.
# If the first line of a file is a header ("# NameOfFile") then everything
#   after the "# " in the first line will be used as the name of the file.
#   Quotes will be put around the name for safety.
# You cannot pre-define the order of anything deeper than tabs. That defeats
#   the purpose of this module.
# Directories that don't contain any nested .md files are ignored.

import os

TARGET_FILE = (
    "mkdocs.yml"  # where to insert the nav (this is so I can use test.yml for testing)
)
DOCS_DIR_PATH = "docs"  # location of your documentation
TAB_ORDER = [
    "index.md",
    "API Reference",
    "Handbook",
    "Concept Art",
]  # ordered list of your tabs
INDEX_MD_NAME = "Home"  # name for the index.md file

path_substring_start_index = len(DOCS_DIR_PATH) + 1


def recurse_tree(path, depth):
    nav_dirs = []
    nav_files = []

    for dirEntry in os.scandir(path):
        if dirEntry.is_dir():
            recurse_string = recurse_tree(dirEntry.path, depth + 1)

            if len(recurse_string) > 0:
                # this is only true when there is a .md nested in this directory
                nav_dirs.append(f"{'  ' * depth}- {dirEntry.name}:\n{recurse_string}")
        elif dirEntry.is_file():
            file_name_tuple = os.path.splitext(dirEntry.path)

            if file_name_tuple[1] == ".md":
                file_name = dirEntry.name.split(".")[0]  # get what's before the .md
                relative_file_path = dirEntry.path[
                    path_substring_start_index:
                ]  # get rid of the root path at the start

                with open(dirEntry.path, "r", errors="ignore") as f:
                    first_line = f.readline().strip()
                    if first_line[0:2] == "# ":
                        nav_files.append(
                            f"{'  ' * depth}- \"{first_line[2:]}\": {relative_file_path}\n"
                        )
                    else:
                        nav_files.append(
                            f"{'  ' * depth}- {file_name}: {relative_file_path}\n"
                        )

    nav_dirs = sorted(nav_dirs)  # sort alphabetically
    nav_files = sorted(nav_files)

    return "".join(nav_files) + "".join(nav_dirs)


nav = "\n\nnav:\n"
for dirEntry in TAB_ORDER:  # add tabs in the pre-defined order
    split = dirEntry.split(".md")
    if len(split) > 1:  # got a file
        if dirEntry == "index.md":  # special case for index.md
            nav += f"  - {INDEX_MD_NAME}: index.md\n"
        else:
            nav += f"  - {split[0]}: {dirEntry}\n"
    else:  # got a directory
        recurse_string = recurse_tree(f"{DOCS_DIR_PATH}/{dirEntry}", 2)
        nav += f"  - {dirEntry}:\n{recurse_string}"

with open(TARGET_FILE, "a") as f:  # append the nav to mkdocs.yml
    f.write(nav)
