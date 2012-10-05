#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 Allan SIMON <allan.simon@supinfo.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import pygtk
pygtk.require('2.0')
import gtk
from constants import *
from qrcode import *

# for the moment this code only display a window containing a valid
# wechat/weixin QRcode

class MainWin:

    def destroy(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()

    def __init__(self):
        # create the main window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(10)

        # this gtk image will contain the QRcode
        self.image=gtk.Image()

        # we load the image from the URL
        loader=gtk.gdk.PixbufLoader()
        loader.write(
            get_qrcode_image()
        )
        loader.close()        
        self.image.set_from_pixbuf(loader.get_pixbuf())

        # we display this image in the main window
        self.window.add(self.image)
        self.image.show()
        self.window.show()

    def main(self):
        gtk.main()

if __name__ == "__main__":
    MainWin().main()






