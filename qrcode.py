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

import urllib2
from lxml import etree
from constants import *

# set of functions to get the QRcode image


# return the URL of the QRcode image
def get_qrcode_full_url():
    #TODO handle connection problem etc.
    # we first open the html page of the webclient
    # that contain the QRcode image
    response = urllib2.urlopen(WEIXIN_QRCODE_PAGE)
    html = response.read()
    
    # we search the img tag ...
    tree = etree.HTML(html)
    for image in tree.xpath("//img"):
        if image.attrib.has_key('class'):
            # ... that contain the QRcode class...
            if QRCODE_TAG_CLASSES in image.attrib['class']:
                imageUrl = image.attrib['src']
                # ... and we return the full url of it
                qrcodeFullUrl = WEIXIN_LOGIN_DOMAIN + imageUrl
                return qrcodeFullUrl


# return a raw binary string of the image
def get_qrcode_image_from_url(qrcodeFullUrl):
    response = urllib2.urlopen(qrcodeFullUrl)
    image = response.read()
    return image

# wrapper function to get the raw binary string
# from the wechat webclient login page
def get_qrcode_image():
    qrcodeFullUrl = get_qrcode_full_url()
    return get_qrcode_image_from_url(qrcodeFullUrl)




