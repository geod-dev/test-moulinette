import os
import subprocess
import importlib.util
import sys
import re

def match(got, expected):
    expected = re.escape(expected.strip()).replace('\\$\\*', '.*')
    return re.match(f'^{expected}$', got.strip()) is not None

root = os.path.dirname(os.path.abspath(__file__)) + "/tests/"
days = []

for folder in os.listdir(root):
    if os.path.isdir(os.path.join(root, folder)):
        days.append(folder)

print("available days:", ", ".join(days))
day = input("which day ?")

folder = os.path.join(root, day)

for test_file in os.listdir(folder):
    if test_file.startswith("test_"):
        test_spec = importlib.util.spec_from_file_location(test_file.replace(".py", ""), os.path.join(folder, test_file))
        test = importlib.util.module_from_spec(test_spec)
        test_spec.loader.exec_module(test)
        output = subprocess.run(test.COMMAND, shell=True, capture_output=True).stdout.decode(sys.stdout.encoding)
        if match(output, test.OUTPUT):
            print(f"TEST {test_file} PASSED !")
        else:
            print(f"TEST {test_file} FAILED !")
            print("\nexpected:")
            print(test.OUTPUT.strip())
            print("\ngot:")
            print(output.strip())
            break
