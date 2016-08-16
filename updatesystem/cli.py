
# -*- coding: UTF-8 -*-

from log import logger as logging

import argparse

def get_parser():
    parser = argparse.ArgumentParser(description="this is update system command \
            line")
    parser.add_argument("--check",action="store_true",
            help="check system status for update")
    parser.add_argument("--install",
            help="install a  patch")
    parser.add_argument("--install-all", action="store_true",
            dest="install_all", help="install all patch")
    
    return parser

if __name__  == "__main__":
    parser = get_parser()
    args = parser.parse_args()
    if args.check:
        print("this is a check")
    if args.install:
        print("install {} ".format(args.install))
    if args.install_all:
        print("install all")
else:
    parser = get_parser()

