import os

def removeFile(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
