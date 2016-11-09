#!/usr/bin/env python
# encoding: utf-8

import requests

def download_image():
    """
    下载图片
    """
    url = "http://image.lxway.com/upload/0/b2/0b2b7eb5ce674e66c6a728e85afae0f3_thumb.jpg"
    response = requests.get(url)
    print ">>>>>>status code:"
    print response.status_code
    with open('demo.jpg','wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)

if __name__ == '__main__':
    download_image()
