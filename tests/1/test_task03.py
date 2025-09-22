import subprocess 
import sys

COMMAND = "./task03/midLS"
OUTPUT = subprocess.run("ls -mp", shell=True, capture_output=True).stdout.decode(sys.stdout.encoding)
