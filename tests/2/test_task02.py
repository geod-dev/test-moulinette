import os

assets = os.path.dirname(os.path.abspath(__file__)) + "/assets"
cwd = os.getcwd()

COMMAND=f"(cd {assets}/test_folder && {cwd}/find_sh.sh)"
OUTPUT="""
./folder/script2.sh
./script1.sh
"""
