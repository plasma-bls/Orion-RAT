import platform
import os
def clr():
    if platform.system() == 'Linux':
        os.system("clear")
    if platform.system() == 'Windows':
        os.system("cls")