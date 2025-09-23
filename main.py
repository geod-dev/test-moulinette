import os
import subprocess
import importlib.util
import sys
import re
import difflib

def match(got, expected):
    expected = re.escape(expected.strip()).replace('\\$\\*', '.*')
    return re.match(f'^{expected}$', got.strip()) is not None

def display_string_diff(string1, string2):
    d = difflib.Differ()
    diff = d.compare(string1.splitlines(), string2.splitlines())
    print('\n'.join(diff))

def check_output(n, output, expected):
    if type(expected) == str:
        return check_single_output(n, output, expected)
    else:
        passed = False
        for e in expected:
            if check_single_output(n, output, e, False):
                passed = True
                break
        if not passed:
            print(f"TEST {n} FAILED !")
            print("\ngot:")
            print(output.strip())
            for e in expected:
                print("\nexpected:")
                print(e)
            print("\n\n")     
        return passed

def check_single_output(n, output, expected, verbose = True):
    if match(output, expected):
        if verbose:
            print(f"TEST {n} PASSED !")
        return True
    if verbose:
        print(f"TEST {n} FAILED !")
        print("\nexpected:")
        print(expected.strip())
        print("\ngot:")
        print(output.strip())
        print("\n\n")
        print(display_string_diff(output, expected))
    return False

root = os.path.dirname(os.path.abspath(__file__)) + "/tests/"
days = []

for folder in os.listdir(root):
    if os.path.isdir(os.path.join(root, folder)):
        days.append(folder)

print("available days:", ", ".join(days))
day = input("which day ?")

folder = os.path.join(root, day)

for test_file in sorted(os.listdir(folder)):
    if test_file.startswith("test_"):
        test_spec = importlib.util.spec_from_file_location(test_file.replace(".py", ""), os.path.join(folder, test_file))
        test = importlib.util.module_from_spec(test_spec)
        test_spec.loader.exec_module(test)
        output = subprocess.run(test.COMMAND, shell=True, capture_output=True).stdout.decode(sys.stdout.encoding)
        if not check_output(test_file, output, test.OUTPUT):
            break
            
