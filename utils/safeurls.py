#!/usr/bin/env python
# encoding: utf-8
from urllib.parse import urlparse,urljoin
from flask import request

def is_safe_url(target):
    # http://127.0.0.1:5000/
    ref_url = urlparse(request.host_url)
    # http://127.0.0.1:5000/register/
    # ParseResult(scheme='http', netloc='127.0.0.1:5000', path='/register/', params='', query='', fragment='')
    test_url = urlparse(urljoin(request.host_url,target))
    return test_url.scheme in ('http','https') and ref_url.netloc == test_url.netloc


# >>>from urllib.parse import urljoin
# >>> urljoin("http://www.chachabei.com/folder/currentpage.html", "anotherpage.html")
# 'http://www.chachabei.com/folder/anotherpage.html'
# >>> urljoin("http://www.chachabei.com/folder/currentpage.html", "/anotherpage.html")
# 'http://www.chachabei.com/anotherpage.html'
# >>> urljoin("http://www.chachabei.com/folder/currentpage.html", "folder2/anotherpage.html")
# 'http://www.chachabei.com/folder/folder2/anotherpage.html'
# >>> urljoin("http://www.chachabei.com/folder/currentpage.html", "/folder2/anotherpage.html")
# 'http://www.chachabei.com/folder2/anotherpage.html'
# >>> urljoin("http://www.chachabei.com/abc/folder/currentpage.html", "/folder2/anotherpage.html")
# 'http://www.chachabei.com/folder2/anotherpage.html'
# >>> urljoin("http://www.chachabei.com/abc/folder/currentpage.html", "../anotherpage.html")
# 'http://www.chachabei.com/abc/anotherpage.html'