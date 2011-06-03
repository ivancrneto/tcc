#!/usr/bin/env python

import os
import sys
import unittest

IGNORE_FILES = ['run_tests.py', '__init__.py']

suite = unittest.TestSuite()
debug = True
tests_path = 'tests'


sys.path.append("./tests")
sys.path.append("./tests/base")

try:
    descriptions = sys.argv[1]
    verbosity = sys.argv[1]
except IndexError:
    descriptions = 2
    verbosity = 2

try:
    if sys.argv[2] == '1':
        debug = True
except IndexError:
    pass

def find_tests(path):
    for file in os.listdir(os.path.abspath(path)):
        if file in IGNORE_FILES:
            continue
        if os.path.isdir(file):
            find_tests(os.path.join(path, file))
            continue
        elif file[-3:] != '.py':
            continue
        if debug: print 'Found test : %s' % file[:-3]
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(file[:-3]))

find_tests(tests_path)

test_runner = unittest.TextTestRunner(descriptions=descriptions, verbosity=verbosity)
result = test_runner.run(suite)
if result.failures or result.errors:
    sys.exit(1)

