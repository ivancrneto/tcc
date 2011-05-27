Logo Maker Example
==================

This example was used in the Creating GUI Applications with PyQt and Qt
Designer presentation at PyCon UK 2007. It shows how custom widgets written in
Python can be made available to Qt Designer in order to make the design process
as intuitive as possible.

The example is designed to be run from the directory in which it is located.
It is not designed to be installed for system-wide use. To run it, simply
launch the main.pyw file from a file browser, or type

  python main.pyw

at the command line.

To view and edit the user interface in Qt Designer, you can either install the
custom widgets and their corresponding plugins as described in the
presentation, or set the PYTHONPATH and PYQTDESIGNERPATH environment variables
to refer to the current directory and the plugins directories respectively.

For example, using the bash shell, you could type the following at the command
line from within the directory containing the UI file:

  export PYTHONPATH=.
  export PYQTDESIGNERPATH=plugins
  designer ui/mainwindow.ui &

If you change the user interface, it will need to be rebuilt before it can be
used in the example. Run the build.py script to generate a new ui_mainwindow.py
file.
