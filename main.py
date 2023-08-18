#! /usr/bin/python3

# TODO rename file to be program name

from src import func
from src import parsers

def main(args):
    # TODO program main program
    pass

if __name__ == '__main__':
    args = parsers.main_parser.parse_args()

    # TODO conditional actions based on specific arguments

    main(args=args)