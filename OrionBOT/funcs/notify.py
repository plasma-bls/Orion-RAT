import os # only linux
def notify(content):
    os.system(f"notify-send '{content}'")