#!/usr/bin/env python
modules ={u'home_frame': [0, '', u'home_frame.py']}

import wx

def init():
    app = wx.App(False)
    frame = wx.Frame(None, wx.ID_ANY, "Navi")
    frame.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()
