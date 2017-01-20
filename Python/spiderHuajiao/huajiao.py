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
    soup = get_soup_by_url(huajiao_main_url)
    hd_nav = soup.find_all('a', {'href': re.compile('category')})
    print('hd_nav: ', hd_nav)
    categories = dict()
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

# 获取直播分类列表数据
def get_category_list(catgory_id):
    catgory_url = "http://www.huajiao.com/category/" + str(catgory_id)
    soup = get_soup_by_url(catgory_url)
    # 获取最大分页数
    last_page_tag = soup.find_all('li', "paginate_button last")[0]
    last_page = int(last_page_tag.get('tabindex')) - 1
    print('last_page: ', last_page)

    return

get_category_list(999)