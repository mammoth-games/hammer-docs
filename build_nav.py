import os

docs_dir_path = "docs"
path_substring_start = len(docs_dir_path) + 1

def recurse_tree(path, depth):
    nav_dirs = []
    nav_files = []

    for dirEntry in os.scandir(path):
        if dirEntry.is_dir():
            recurse_string = recurse_tree(dirEntry.path, depth + 1)
            
            if len(recurse_string) > 0:
                # this is only true when there is a nested .md in this directory
                nav_dirs.insert(0, "  " * depth + "- " + dirEntry.name + ":\n" + recurse_string)
        elif dirEntry.is_file():
            file_name_tuple = os.path.splitext(dirEntry.path)
            
            if file_name_tuple[1] == ".md":
                file_name = dirEntry.name.split(".")[0] # get what's before the .md

                if file_name == "index" and depth == 1:
                    nav_files.insert(0, "  - Home: indexs.md\n")
                else:
                    relative_file_path = dirEntry.path[path_substring_start:] # get rid of the root path at the start
                    nav_files.insert(0, "  " * depth + "- " + file_name + ": " + relative_file_path + "\n")
    
    nav_dirs = sorted(nav_dirs) # sort alphabetically
    nav_files = sorted(nav_files)

    return "".join(nav_dirs) + "".join(nav_files)

nav = "\n\nnav:\n" + recurse_tree(docs_dir_path, 1)

with open("mkdocs.yml", "a") as f: # append the nav to mkdocs.yml
    f.write(nav)