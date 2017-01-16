import requests
from bs4 import BeautifulSoup
import re
import ast
import json

url = "http://huaban.com/boards/19232159/"
html = requests.get(url)
plain_text = html.text
soup = BeautifulSoup(plain_text, 'html.parser')


app = {"page":{}}

for script in soup.findAll('script'):
    regex = re.compile(r'\w*app.page\["board"]\w*')
    if regex.findall(str(script)):
        # print('>>>>>>>>>>>>>', script)
        app = str(script)[8:len(str(script)) - 9]
        app = app.replace('var', '').replace(';', '')
        app = app.replace('var', '').replace(';', '').replace('app.route()', '').replace('view = app.view = $("page").hide()', '').replace('app._csr = true', '').replace('\n', '').replace('app = app || {}', 'app={"page":{}}')
        app = app.replace('app.page = app.page || {}', 'app.page = {}').replace('app={"page":{}}app.page = {}app.page["$url"] = "/boards/19232159/"app.page["board"] = ','')
        # result = dict()
        result = u'' + str(app)

        # result = json.loads(result)
        print(result)
