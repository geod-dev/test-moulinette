import os

assets = os.path.dirname(os.path.abspath(__file__)) + "/assets"
cwd = os.getcwd()

COMMAND=f"cat {assets}/passwd | ./gotta_catch_them_all.sh 'der'"
OUTPUT="45"
