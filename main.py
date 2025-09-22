import os
import subprocess
import importlib.util
import sys

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
        if output.strip() == test.OUTPUT.strip():
            print(f"TEST {test_file} PASSED !")
        else:
            print(f"TEST {test_file} FAILED !")
            print("expected:")
            print(test.OUTPUT)
            print("\n\ngot:")
            print(output)
            break
