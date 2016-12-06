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
def download_image_improved():
    #如果没有权限 伪造header {'User-Agent':}
    url = "http://image.lxway.com/upload/0/b2/0b2b7eb5ce674e66c6a728e85afae0f3_thumb.jpg"
    from contextlib import closing
    #关闭流
    with closing(requests.get(url,stream=True)) as response:
        with open('demo1.jpg','wb') as fd:
            for chunk in response.iter_content(128):
                fd.write(chunk)



if __name__ == '__main__':
    download_image_improved()
