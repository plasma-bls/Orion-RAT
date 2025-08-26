import os # only linux

# NOTE: Can be a extension, and not a internal func. This pollute the codebase

def notify(content):
    os.system(f"notify-send '{content}'")
