#! /usr/bin/python3

import argparse

class Parsers:
    # Variables #
    main_parser = None

    def __init__(self):
        self.main_parser = argparse.ArgumentParser(
            # TODO Update with what the program does
            description='',
            # TODO program shell located in program root, ie ./program
            prog='',
        )

        # TODO add arguments