import subprocess
import platform
import sys
import os

try:
    system = platform.system()
    # command to run Python environment
    if system == "Windows":
        command = "python -m venv venv"
    elif system == "Linux" or system == "Darwin":
        command = "python3 -m venv venv"


    # execute the command
    subprocess.run(command, shell=True, check=True)

    # activate the environment
    if system == "Windows":
        activate_script = "venv\\Scripts\\activate.bat"
    elif system == "Linux" or system == "Darwin":
        activate_script = "source venv/bin/activate"
    subprocess.run(activate_script, shell=True, check=True)

    # check if requirements are already installed
    if system == "Windows":
        reqs = subprocess.check_output(['pip', 'freeze']).decode('utf-8')
    elif system == "Linux" or system == "Darwin":
        reqs = subprocess.check_output(['pip3', 'freeze']).decode('utf-8')
    with open('requirements.txt', 'r') as f:
        requirements = f.read()
    if requirements not in reqs:
        # install the requirements
        if system == "Windows":
            subprocess.run("pip install -r requirements.txt", shell=True, check=True)
        elif system == "Linux" or system == "Darwin":
            subprocess.run("pip3 install -r requirements.txt", shell=True, check=True)
        subprocess.run(activate_script, shell=True, check=True)
        

    # run the gpt-plus.py script
    if system == "Windows":
        subprocess.run("python gpt-plus.py", shell=True, check=True)
    elif system == "Linux" or system == "Darwin":
        subprocess.run("python3 gpt-plus.py", shell=True, check=True)
    

    # Exit virtual environment
    subprocess.run(["exit"], shell=True, check=True)

except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")
    