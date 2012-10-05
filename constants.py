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


#this file is here only to contain constant
#no logical code is stored in it, the goal is to be able
#to easily adapt the code in case weixin change their API id etc.

WEIXIN_LOGIN_DOMAIN =  'https://login.wechatapp.com'
WEIXIN_LOGIN_PAGE = '/qrlogin?appid='
WEIXIN_APPID = 'wx782c26e4c19acffb'
QRCODE_TAG_CLASSES = 'qrcode'

# the url of the html page that contains in it the qrcode image
WEIXIN_QRCODE_PAGE = WEIXIN_LOGIN_DOMAIN + WEIXIN_LOGIN_PAGE + WEIXIN_APPID


