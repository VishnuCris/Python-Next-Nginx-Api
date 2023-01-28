# from subprocess import Popen, PIPE
import os
import subprocess

# subprocess.call(['df','-h'])
def updateRquirement_txt(file_name,package_file="../requirements.txt"):
	result = ''
	for path in execute(["git","diff",file_name]):
		result+=path
	if result:
		os.system(f"pip freeze > {package_file}")
		print(f"{package_file} file is updated")
	else:
		print(f"No Changes detected in file {file_name}")


def execute(cmd):
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line 
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)

def updateRquirement_txt_easy(file_name,package_file="../requirements.txt"):
	process = subprocess.Popen(['git','diff', file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout, stderr = process.communicate()
	if stdout.decode():
		os.system(f"pip freeze > {package_file}")
		print(f"{package_file} file is updated")
	else:
		print(f"No Changes detected in file {file_name}")

