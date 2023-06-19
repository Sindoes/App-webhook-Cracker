import os
def reboot(seconds):
    os.system("shutdown /r -t "+seconds)
def shutdown():
    os.system("shutdown /s")
def signout():
    os.system("shutdown /l")