#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "luisfff"


import sys
import argparse


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


def func_lower(text):
    return text.lower()


def func_upper(text):
    return text.upper()


def func_title(text):
    return text.title()


def main():
    """Implementation of echo"""
    parser = create_parser()
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
