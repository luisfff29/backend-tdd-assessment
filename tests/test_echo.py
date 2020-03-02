#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess
# Python program to print all combinations
from itertools import permutations

# Your test case class goes here


def all_options():
    """Return list of all combinations length 3 and 2"""
    # All combinations, group of 3
    g3 = permutations('ult')
    group3 = [i for i in list(g3)]

    # All combinations, group of 2
    g2 = permutations('ult', 2)
    group2 = [i for i in list(g2)]

    # group2 is now inside group3
    group3.extend(group2)
    return list('-' + ''.join(i) for i in group3)


class TestEcho(unittest.TestCase):
    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_upper_1(self):
        self.assertEqual(echo.func_upper('hello'), 'HELLO')

    def test_lower_1(self):
        self.assertEqual(echo.func_lower('Hello'), 'hello')

    def test_title_1(self):
        self.assertEqual(echo.func_title('hello'), 'Hello')

    def test_all_1(self):
        for op in all_options():
            output = subprocess.check_output(
                ["python", "echo.py", op, "heLLo!"])
            if 't' not in op:
                self.assertEqual(output.rstrip(), 'hello!')
                continue
            self.assertEqual(output.rstrip(), 'Hello!')

    def test_no_args_1(self):
        self.assertEqual(echo.func_no_args('hElLo'), 'hElLo')


if __name__ == '__main__':
    unittest.main()
