#!/usr/bin/env python

import os

commands = ("pyuic4 -o ui_mainwindow.py ui/mainwindow.ui",
            )

for command in commands:
    print command
    os.system(command)
