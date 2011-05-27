Creating GUI Applications with PyQt and Qt Designer
===================================================

The files included in this directory contain the source material used to create
the PDF version of the talk, and also include the interactive slideshow tool
used during the presentation.

To view the presentation using the slideshow tool, simply launch the
slideshow.pyw file from a file browser, or type

  python slideshow.pyw

at the command line. The natural size of the window is quite large, so it may
help to display the slides in full-screen mode (press Ctrl+F to toggle this).
You can exit the slideshow at any time by pressing Ctrl+Q.

To view and edit the contents of the presentation in Qt Designer, you can
either install the custom widgets and their corresponding plugins as described
in the presentation, or set the PYTHONPATH and PYQTDESIGNERPATH environment
variables to refer to the Plugins/widgets and Plugins/python directories
respectively.

For example, using the bash shell, you could type the following at the command
line from within the directory containing the UI file:

  export PYTHONPATH=Plugins/widgets
  export PYQTDESIGNERPATH=Plugins/python
  designer PyCon_UK_PyQt_Qt_Designer.ui &

If you change the user interface, it will need to be rebuilt before it can be
used in the slideshow. Run the build.py script to generate a new ui_slides.py
file.
