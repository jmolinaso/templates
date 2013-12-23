#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
import argparse

def main():
    parser = argparse.ArgumentParser(description="Template to create command line python applicaions")
    parser.add_argument("-d","--debug",help="Enable debugging",action="store_true")
    parser.add_argument("-s","--something",help="Regular parameter")
    arguments = parser.parse_args()
    # Logging section
    if arguments.debug:
        logging.basicConfig(format='%(asctime)s [%(levelname)s] [%(module)s::%(funcName)s] %(message)s', level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(asctime)s [%(levelname)s] [%(module)s::%(funcName)s] %(message)s', level=logging.INFO)

    logging.debug("Argument something =  %s",arguments.something)
    actual_code()

def actual_code():
    logging.info("Starting %s",__file__)
    logging.info("End %s",__file__)

if __name__ == '__main__':
    main()
