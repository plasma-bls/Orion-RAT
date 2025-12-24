import PIL
from PIL import ImageGrab
import platform
import os
if platform.system() == "Linux":
    def sgrab():
            screenshot = ImageGrab.grab()
            screenshot.save('/tmp/sys.png')
            screenshot.close()
    def sdelete():
        os.remove('/tmp/sys.png')
    sgrab()

if platform.system() == "Windows":
    def sgrab():
            screenshot = ImageGrab.grab()
            screenshot.save(f'C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp\\sys.png')
            screenshot.close()
    def sdelete():
        os.remove(f'C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp\\sys.png')
    sgrab()