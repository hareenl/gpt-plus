import subprocess
import platform
import pathlib

# Check if virtual environment exists
if not pathlib.Path("venv").exists():
    # Create virtual environment
    subprocess.run(["python3", "-m", "venv", "venv"])

    # Activate virtual environment
    if platform.system() == "Windows":
        activate_script = "venv\\Scripts\\activate.bat"
    else:
        activate_script = "source venv/bin/activate"
    subprocess.run(activate_script, shell=True)

    # Install required packages inside virtual environment
    subprocess.run(["pip3", "install", "-r", "requirements.txt"])

    # Deactivate virtual environment
    subprocess.run(["deactivate"], shell=True)

# Activate virtual environment
if platform.system() == "Windows":
    activate_script = "venv\\Scripts\\activate.bat"
else:
    activate_script = "source venv/bin/activate"
subprocess.run(activate_script, shell=True)

# Run your code
subprocess.run(["python3", "gpt-plus.py"])

# Deactivate virtual environment
subprocess.run(["deactivate"], shell=True)