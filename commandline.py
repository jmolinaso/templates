#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Template to create command line python applicaions")
    parser.add_argument("-v","--verbose",help="Example switch",action="store_true")
    parser.add_argument("-s","--something",help="Regular parameter")
    arguments = parser.parse_args()
    if arguments.verbose:
        print "Got a verbosed"
    print "Argument: " + arguments.something
