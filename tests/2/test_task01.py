import os

assets = os.path.dirname(os.path.abspath(__file__)) + "/assets"

COMMAND=f"cat {assets}/students.csv | ./how_many_are_we.sh par"
OUTPUT="1245"
