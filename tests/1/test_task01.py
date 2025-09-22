import getpass

user = getpass.getuser()

COMMAND = "ls -l --no-group task01"

OUTPUT = f"""
total 8
-rw-rw-r-- 1 {user}  0 Sep 22 10:58 test01
-rwxrwxr-x 1 {user} 41 Sep 22 15:24 test02
lrwxrwxrwx 1 {user}  6 Sep 22 14:08 test03 -> test02
"""
