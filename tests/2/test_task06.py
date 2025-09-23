import os

assets = os.path.dirname(os.path.abspath(__file__)) + "/assets"
cwd = os.getcwd()

COMMAND=f"(cd {assets}/test_folder && ls | {cwd}/skip.sh | cat -e)"
OUTPUT="""
file1$
folder$
"""
