import os

def get_dir() -> str:
    return os.getcwd()

def list_directory(directory=get_dir()) -> list[str]:
    return os.listdir(path=directory)

def change_directory(directory: str):
    os.chdir(directory)
