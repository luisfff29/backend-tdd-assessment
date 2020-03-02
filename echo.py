#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "luisfff29"

import sys
import argparse
import subprocess


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    parser.add_argument('text', help='text to be manipulated')
    parser.add_argument('-u', '--upper', action='store_true',
                        help='convert text to uppercase')
    parser.add_argument('-l', '--lower', action='store_true',
                        help='convert text to lowercase')
    parser.add_argument('-t', '--title', action='store_true',
                        help='convert text to titlecase')
    return parser


def func_upper(text):
    """convert text to uppercase"""
    return text.upper()


def func_lower(text):
    """convert text to lowercase"""
    return text.lower()


def func_title(text):
    """convert text to titlecase"""
    return text.title()


def func_no_args(text):
    output = subprocess.check_output(['python', 'echo.py', text])
    return output.rstrip()


def main():
    """Implementation of echo"""
    parser = create_parser()
    args = parser.parse_args()

    if not args:
        parser.print_usage()
        sys.exit(1)

    result = args.text
    if args.upper:
        result = func_upper(args.text)

    if args.lower:
        result = func_lower(args.text)

    if args.title:
        result = func_title(args.text)

    print(result)


if __name__ == '__main__':
    main()
