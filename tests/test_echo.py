#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess

# Your test case class goes here


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


if __name__ == '__main__':
    unittest.main()
