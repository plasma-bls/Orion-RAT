import requests
import os
def clean():
    filelist=os.listdir('fnlstager/')
    for i in filelist:
        os.remove(f"fnlstager/{i}")
