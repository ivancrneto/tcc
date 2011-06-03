#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
from base.makecoba import Project

class MakecobaProjectTestCase(unittest.TestCase):
    def setUp(self):
        self.project_name = 'project_name'
        self.project_path = '/home/ivan/UFBA/pf2/tcc/navi/tests/trash'
        self.project = Project('project_test')
        
    def tearDown(self):
        self.project.dispose()
        
    def test_project_data(self):
        assertEqual(self.project.name, self.project_name, 'The project name is wrong')
        assertEqual(self.project.path, self.project_path, 'The project path is wrong')
        
        
if __name__ == '__main__':
    unittest.main()


