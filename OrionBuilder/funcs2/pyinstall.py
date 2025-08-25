import os
def convert(filename):
    os.system(f"pyinstaller --onefile --clean --noconfirm --log-level=ERROR {filename}")
