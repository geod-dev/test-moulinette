import getpass

user = getpass.getuser()

COMMAND = "ls -l --no-group task01"

OUTPUT = f"""
total 8
-rw-rw-r-- 1 {user}  0 $* test01
-rwxrwxr-x 1 {user} 41 $* test02
lrwxrwxrwx 1 {user}  6 $* test03 -> test02
"""
