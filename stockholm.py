#!/usr/bin/env python3

import argparse
from os import environ
from os import path
import os

args : None

def exit_error(error: str):
    prints(error)
    exit(1)

def prints(str_to_print: str):
    global args
    if not args.silent:
        print(str_to_print)

def parse_args():
    global args
    parser = argparse.ArgumentParser(description="This randsomware will encode file at ~/infection/ whose extensions have been affected by Wannacry")
    parser.add_argument("-v", '--version', action='version', version='%(prog)s 1.0')
    parser.add_argument("-r", '--reverse', action='store_true', help="Decode encoded files")
    parser.add_argument('-s', '--silent', action='store_true', help='Execute in silent mode')
    args =  parser.parse_args()

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


def main():
    parse_args()
    check_dir()

if __name__ == "__main__":
    main()