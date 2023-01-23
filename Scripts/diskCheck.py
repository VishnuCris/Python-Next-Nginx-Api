# from subprocess import Popen, PIPE
import os
import subprocess

# subprocess.call(['df','-h'])
def push_remote(msg):
	# subprocess.call(['cd','/Documents/Backend/python/flask/StudentsManagementApi/'])
	subprocess.call(['git','status'])
	# subprocess.call(['git','add .'])
	subprocess.call(['git',"commit -a -m"])
	subprocess.call(['git','push'])
