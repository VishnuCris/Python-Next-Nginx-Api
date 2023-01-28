# from subprocess import Popen, PIPE
import os
import subprocess

# subprocess.call(['df','-h'])
def updateRquirement_txt(file_name):
	subprocess.run(["git", 'diff','../__init__.py'])
