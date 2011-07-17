#!/usr/bin/env python

import os

commands = ("pyuic4 -o ../ui/mainwindow.py mainwindow.ui",
            "pyuic4 -o ../ui/new_project.py new_project.ui")

for command in commands:
    print command
    os.system(command)
