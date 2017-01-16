import requests
from bs4 import BeautifulSoup
import re

url = "http://huaban.com/boards/19232159/"
html = requests.get(url)
plain_text = html.text
soup = BeautifulSoup(plain_text, 'html.parser')


for script in soup.findAll('script'):
    regex = re.compile(r'\w*app.page\["board"]\w*')
    if regex.findall(str(script)):
        print('>>>>>>>>>>>>>', script)
