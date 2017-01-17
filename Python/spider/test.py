import requests
from bs4 import BeautifulSoup
import re
import json
import random
import urllib.request

def download_web_iamge(url, file_name):
    full_name = str(file_name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)




def download_huaban_image_by_userId(userid):

    url = "http://huaban.com/boards/"+userid+"/"
    html = requests.get(url)
    print('html: ', html)

    plain_text = html.text
    print('plain_text: ', plain_text)

    soup = BeautifulSoup(plain_text, 'html.parser')


    # app = {'page': {"hello": 1, "world": 2}}
    # print(app['page']['hello'])

    for script in soup.findAll('script'):
        regex = re.compile(r'\w*app.page\["board"]\w*')
        if regex.findall(str(script)):
            # print('>>>>>>>>>>>>>', script)
            app = str(script)[8:len(str(script)) - 9]
            app = app.replace('var', '').replace(';', '').replace('app.route()', '').replace('view = app.view = $("page").hide()', '').replace('app._csr = true', '').replace('\n', '').replace('app = app || {}', 'app={"page":{}}')
            app = app.replace('app.page = app.page || {}', 'app.page = {}').replace('app={"page":{}}app.page = {}app.page["$url"] = "/boards/'+userid+'/"app.page["board"] = ', '')
            # result = dict()
            result = u'' + str(app)
            print('result: ', result)

            obj = json.loads(result)
            pins = obj['pins']
            print('pins: ', pins)
            # pin_id file:{id, key, width,height}
            # image_url: http://hbimg.b0.upaiyun.com/key

download_huaban_image_by_userId(19232159)
