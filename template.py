import os
from pathlib import Path 
import logging

logging.basicConfig(level= logging.INFO, format="[%(asctime)s]: %(message)s:")

list_of_files=[

    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",  
    "requirements.txt",  
    ".env", 
    "setup.py", 
    "notebook/trails.ipynb",  
    "app.py",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "store_index.py",
    "static",
    "templates/chat.html"
    
]

for file in list_of_files:
    filepath = Path(file) # creates your system compatible filepath (windows/mac/ubantu etc)
    filedir, filename = os.path.split(filepath)
    # if filedir not empty, create directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # else overwrite
        logging.info(f"creating directory {filedir} for the file filename {filename}")
        
    # if path doesn't exist or pathsize=0, create empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filename)==0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"creating empty file {filepath}")
    else:
        print(f"{filename} already present in:{filedir}")