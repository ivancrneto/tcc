#!/usr/bin/env python

import os

commands = ("pyuic4 -o ui_slides.py PyCon_UK_PyQt_Qt_Designer.ui",
            "pyrcc4 -o PyCon_UK_PyQt_Qt_Designer_rc.py PyCon_UK_PyQt_Qt_Designer.qrc")

for command in commands:
    print command
    os.system(command)
