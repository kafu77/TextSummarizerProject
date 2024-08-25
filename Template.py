import os
from pathlib import Path
import logging

#Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

#Creating a source (SRC) folder
project_name = 'TextSummarizer'

#list of source files to be processed

list_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "test.py",
    "ignore.py"
            
    
]


for filepath in list_files:
    filepath= Path(filepath)
    fileDir, filename =os.path.split(filepath)
    
    if fileDir != "":
        os.makedirs(fileDir, exist_ok=True)
        logging.info(f"Creating directory: {fileDir}:for the file {filename}")
    
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"{filepath} already exists")
    
