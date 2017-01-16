from dict import add

add()

import random
import urllib.request

def download_web_iamge(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_iamge("http://img.hb.aicdn.com/86591874e81a53efa1dc66fb9c947648ed0fcca94fd78-HkqIrt_fw658")

# http://xiaodongli0.wixsite.com/helloworld
