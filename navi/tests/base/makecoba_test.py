#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
from base.makecoba import Project

class MakecobaProjectTestCase(unittest.TestCase):
    def setUp(self):
        self.project_name = 'project_name'
        self.project_path = '/home/ivan/UFBA/pf2/tcc/navi/tests/trash'
        self.project = Project(self.project_name, self.project_path)
        
    def tearDown(self):
        pass
        
    def test_project_data(self):
        self.assertEqual(self.project.name, self.project_name, 'The project name is wrong')
        self.assertEqual(self.project.path, self.project_path, 'The project path is wrong')
        
        
if __name__ == '__main__':
    unittest.main()


