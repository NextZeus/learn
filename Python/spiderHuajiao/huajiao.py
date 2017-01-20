from bs4 import BeautifulSoup
import requests
import re

def get_soup_by_url(url):
    html = requests.get(url)
    plain_text = html.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    return soup

# 获取花椒直播所有分类
def get_huajiao_video_categories():
    huajiao_main_url = "http://www.huajiao.com/"
    home_soup = get_soup_by_url(huajiao_main_url)
    hd_nav = home_soup.find_all('a', {'href': re.compile('category')})
    print('hd_nav: ', hd_nav)
    categories = dict()
    print(len(hd_nav))
    for tag in hd_nav:
        des = tag.string
        if des == '更多>':
            continue
        print('des: ', des)
        print('name:', tag.string)
        category = tag.get('href')[10:]
        print('category: ', category)
        categories[category] = des
    print('categories:', categories)

# get_huajiao_video_categories()

