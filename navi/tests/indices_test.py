# -*- coding: utf-8 -*-

import unittest

from base.indices import Indices

class IndicesCalculationTestCase(unittest.TestCase):
    def setUp(self):
        self.indices = Indices()
    

    def tearDown(self):
        self.indices.dispose()
        self.indices = None

    def test_assortativity(self):
        #assert x != y;
        #self.assertEqual(x, y, "Msg");
        self.fail("TODO: Write test")

    def test_clusterization(self):
        self.fail('TODO: Write test')

if __name__ == '__main__':
    unittest.main()

