import os
import platform
def run(content, title):
    if platform.system() == "Linux":
        os.system(f'notify-send "{title}" "{content}"')
    if platform.system() == "Windows":
        from ctypes import windll, c_wchar_p
        MessageBox = windll.user32.MessageBoxW
        MessageBox(None, c_wchar_p(content), c_wchar_p(title), 0)
