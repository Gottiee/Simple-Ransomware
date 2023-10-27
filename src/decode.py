from utilities import *
import subprocess
import os

def rename(path):
    os.remove(path)

def do_decode(path):
    command = [
        "openssl",
        "enc",
        "-aes-256-cbc",
        "-d", 
        "-pbkdf2",
        "-in", path,
        "-out", path[:-3], 
        "-k", key
    ]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        exit_error("Opensll error during encoding")
    prints(f"{path}: decoded")

def decode(lst: list):
    been_encoded = 0
    prints('\nStart decoding:')
    for file in lst:
        root, extension = os.path.splitext(file)
        if extension != ".ft":
            continue
        do_decode(file.path)
        rename(file.path)
        been_encoded += 1 
    if not been_encoded:
        prints("\tNo file to decode")