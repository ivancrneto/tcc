#!/usr/bin/env python

import os

command = "pyuic4 -o ui_window.py ui/window.ui"
print command
os.system(command)
