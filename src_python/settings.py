"""
Configuration file defining absolute paths to directories

Authors:
    Pedro López Sancha - 2024/03/11
"""
import json
import os.path
import sys

# Construct absolute path to the directory containing the project. This 
# path is stored in _PROJECT_PATH
_PROJECT_NAME = "msc_code"                      # Project folder
_PROJECT_PATH = os.path.normpath(__file__)      # Project dir abs path
_PROJECT_PATH = _PROJECT_PATH.split(os.sep)
try:
    _PROJECT_PATH = os.sep.join(_PROJECT_PATH[: 1 + _PROJECT_PATH.index(_PROJECT_NAME)])
except ValueError as error:
    # Raised if _PROJECT_NAME is not a path component in _PROJECT_PATH
    print(f"{type(error).__name__}: {error}. Failed to resolve absolute path to the project folder")
    print(f"Default project directory name is {_PROJECT_NAME}")
    print(f"Current module path is {__file__}")
    print(f"Default project directory name {_PROJECT_NAME} must be a path component in {__file__}")
    print(f"Reconsider renaming the project directory or changing the default project directory name by editing constant '_PROJECT_NAME' in module {__file__}")
    sys.exit(1)
    
# Configuration file conf.json path, directly stored in the project dir
_CONF_FILE_PATH = os.path.join(_PROJECT_PATH, "conf", "conf.json")
if not os.path.isfile(_CONF_FILE_PATH):
    raise FileNotFoundError(f"Could not find configuration file 'conf.json'. Path: {_CONF_FILE_PATH}")

with open(_CONF_FILE_PATH) as file:
    _conf_file = json.load(file)

# Define paths to common directories and files 
DATA_DIR        = os.path.join(_PROJECT_PATH, _conf_file["directories"]["data"])
SRC_PYTHON_DIR  = os.path.join(_PROJECT_PATH, _conf_file["directories"]["src_python"])
PRIMES_DIR      = os.path.join(DATA_DIR, _conf_file["directories"]["primes"])
PRIMES_FILE     = os.path.join(PRIMES_DIR, _conf_file["files"]["primes"])