#!/usr/bin/env python

import os

commands = ("pyuic4 -o ../ui/mainwindow.py mainwindow.ui",
            "pyuic4 -o ../ui/new_project.py new_project.ui",
            "pyuic4 -o ../ui/choose_sequences.py choose_sequences.ui",
            "pyuic4 -o ../ui/matrices.py matrices.ui",
            "pyuic4 -o ../ui/generate_matrices.py generate_matrices.ui",
            "pyuic4 -o ../ui/image_dialog.py image_dialog.ui",
            "pyuic4 -o ../ui/analyse_threshold_dialog.py analyse_threshold_dialog.ui",)

for command in commands:
    print command
    os.system(command)
