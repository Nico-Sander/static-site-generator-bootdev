import os
import shutil
from generate_page import generate_page


def main():
    clean_copy_to_public()
    generate_page("content/index.md", "template.html", "public/index.html")


def clean_copy_to_public():
    # Get an empty public directory
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public")

    if os.listdir("public") != []:
        raise Exception("public/ directory is not empty.")

    # Copy files from static to public recursively
    if os.path.exists("static") and os.listdir("static") != []:
        copy_recursive("static", "public")

def copy_recursive(src_path, dest_path):
    src_subpaths = os.listdir(src_path)
    src_subpaths, dest_subpaths = [os.path.join(src_path, i) for i in src_subpaths], [os.path.join(dest_path, i) for i in src_subpaths]

    for i in range(len(src_subpaths)):
        if os.path.isfile(src_subpaths[i]):
            shutil.copy(src_subpaths[i], dest_subpaths[i])
        else:
            os.mkdir(dest_subpaths[i])
            copy_recursive(src_subpaths[i], dest_subpaths[i])
    






if __name__ == "__main__":
    main()
