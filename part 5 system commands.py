#oss module has function called system which allow us to run system commands
#Please note this command only exists on Linux and Mac OS X. For Windows use the dir command
import os
os.system("date")

if os.name == 'posix':
    os.system('ls')
else:
    print("The 'ls' command is not available on Windows. Use 'dir' instead.")

# For Windows, use the `dir` command to list files in the directory
if os.name == 'nt':
    os.system('dir')
else:
    print("The 'dir' command is not available on Linux/Mac. Use 'ls' instead.")