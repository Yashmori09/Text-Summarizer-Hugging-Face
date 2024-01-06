import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO,format='[%(asctime)s] : %(message)s')


project_name= "textSummarizer"


list_of_files= [

    ".github/workflows/.gitkeep/",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
]


for file in list_of_files:
    file_path=Path(file)
    folder_name,file_name = os.path.split(file_path)

    if folder_name != '':
        os.makedirs(folder_name,exist_ok=True)
        logging.info(f"Created directory : {folder_name} for the file {file_name}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        logging.info(f"Creating file : {file_path}")
        with open(file_path, "w") as f:
            f.write("")
        logging.info(f"Created file : {file_path}")

    else:
        logging.info(f"File already exists : {file_path}")