import os

assets = os.path.dirname(os.path.abspath(__file__)) + "/assets"
cwd = os.getcwd()

COMMAND=f"(cd {assets}/test_folder && {cwd}/count_files.sh)"
OUTPUT="5"
