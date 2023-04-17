import subprocess
import platform
import sys
import os

try:
    # command to run Python environment
    command = "python3 -m venv venv"

    # execute the command
    subprocess.run(command, shell=True, check=True)

    # activate the environment
    system = platform.system()
    if system == "Windows":
        activate_script = "venv\\Scripts\\activate.bat"
    elif system == "Linux" or system == "Darwin":
        activate_script = "source venv/bin/activate"
    subprocess.run(activate_script, shell=True, check=True)

    # check if requirements are already installed
    reqs = subprocess.check_output(['pip3', 'freeze']).decode('utf-8')
    with open('requirements.txt', 'r') as f:
        requirements = f.read()
    if requirements not in reqs:
        # install the requirements
        subprocess.run("pip3 install -r requirements.txt", shell=True, check=True)

    # run the gpt-plus.py script
    subprocess.run("python3 gpt-plus.py", shell=True, check=True)

    # Exit virtual environment
    subprocess.run(["exit"], shell=True, check=True)

except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")
