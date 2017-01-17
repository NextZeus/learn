import requests
from bs4 import BeautifulSoup
import re
import json
import urllib.request

def download_web_iamge(url, file_name):
    full_name = str(file_name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

def replace_script_variable(script, board_id):
    script = str(script)[8:len(str(script)) - 9]
    script = script.replace('var', '')\
        .replace(';', '')\
        .replace('app.route()', '')\
        .replace('view = app.view = $("page").hide()', '')\
        .replace('app._csr = true', '')\
        .replace('\n', '')\
        .replace('app = app || {}', 'app={"page":{}}')\
        .replace('app.page = app.page || {}', 'app.page = {}')\
        .replace('app={"page":{}}app.page = {}app.page["$url"] = "/boards/' + str(board_id) + '/"app.page["board"] = ', '')

    return script



def download_huaban_image_by_userId(board_id):
    base_image_url = 'http://hbimg.b0.upaiyun.com/'
    url = "http://huaban.com/boards/"+str(board_id)+"/"
    html = requests.get(url)
    plain_text = html.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    for script in soup.findAll('script'):
        regex = re.compile(r'\w*app.page\["board"]\w*')
        if regex.findall(str(script)):
            app = replace_script_variable(script, board_id)
            result = u'' + str(app)
            # print('result: ', result)
            obj = json.loads(result)
            # print('obj: ', obj)
            pins = obj['pins']
            print('pins.length: ', len(pins))

            for pin in pins:
                print('pin:', pin['pin_id'], 'http://hbimg.b0.upaiyun.com/'+pin['file']['key'])
                image_name = pin['file']['key']
                image_url = base_image_url + image_name
                file_name = image_name[len(image_name) - 6:]
                print('file_name', file_name)
                # download_web_iamge(image_url, file_name)
            # pin_id file:{id, key, width,height}
            # image_url: http://hbimg.b0.upaiyun.com/key

# download_huaban_image_by_userId(19232159)
# http://huaban.com/boards/19232159/
# http://huaban.com/ixncm9wj4d/

def parse_categories_script(script):
    script = str(script)[8:len(str(script)) - 9]
    script = script.replace('var', '') \
        .replace('\n', '')\
        .replace('app.route()', '')\
        .replace('view = app.view = $("page").hide()', '')\
        .replace('app._csr = true', '')\
        .replace('app = app || {}', '')\
        .replace('app.page["$url"] = "/categories/', '')\
        .replace('app.render("base/categories", view, function(code, html){view.show();});', '')\
        .replace('"app.page["categories"] = ', '')\

    return script

# 获取花瓣网分类页面
def get_huaban_caregories():
    url = "http://huaban.com/categories/"
    html = requests.get(url)
    plain_text = html.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    for script in soup.findAll('script'):
        regex = re.compile(r'\w*app.page\["categories"]\w*')
        if regex.findall(str(script)):
            app = parse_categories_script(script)
            result = u'' + str(app)
            print('result: ', result)
            obj = json.loads(result)
            print('obj: ', obj)


get_huaban_caregories()