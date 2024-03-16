import os

def removeFile(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"Removed file {file_name}")