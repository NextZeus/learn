from bs4 import BeautifulSoup
from bs4 import NavigableString
import requests
import re

def get_soup_by_url(url):
    html = requests.get(url)
    plain_text = html.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    return soup

# 获取花椒直播所有分类id
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
        # print('des: ', des)
        # print('name:', tag.string)
        category = tag.get('href')[10:]
        # print('category: ', category)
        categories[category] = des
    print('categories:', categories)

# 根据 分类id 和 页码 获取对应请求的url
def get_category_url_by_id_and_pageno(catgory_id, pageno):
    catgory_url = "http://www.huajiao.com/category/" + str(catgory_id) + "pageno=" + str(pageno)
    return catgory_url

# 获取直播分类列表数据
def get_category_list(catgory_id):
    catgory_url = "http://www.huajiao.com/category/" + str(catgory_id)
    soup = get_soup_by_url(catgory_url)
    # 获取最大分页数
    last_page_tag = soup.find_all('li', "paginate_button last")[0]
    last_page = int(last_page_tag.get('tabindex'))
    print('last_page: ', last_page)

    data = list()

    for pageno in range(1, last_page):
        print('page: ', pageno)
        catgory_url = get_category_url_by_id_and_pageno(catgory_id, pageno)
        soup = get_soup_by_url(catgory_url)
        main_list = soup.find_all('a', href=re.compile('/l/'))

        for link in main_list:
            person = dict()
            userId = link.get('href')[3:]
            person['userId'] = userId
            children = link.children

            for child in children:
                # child是最外层的两个div

                if not isinstance(child, NavigableString):
                    attr = child.attrs['class'][0]
                    if attr == 'pic':
                        avatar = child.img.get('src')
                        person['avatar'] = avatar
                        # print('avatar: ', avatar)
                    elif attr == 'text':
                        # 第一个div 主播昵称
                        nickName = child.div.get_text()
                        person['nickName'] = nickName
                        # 获取span里的正在观看人数
                        watches = child.find_all('span', 'num')[0].get_text()
                        person['watches'] = watches
                        # print('nickName: ', nickName)
                        # print('watches: ', watches)
                    else:
                        print('continue!')
            data.append(person)
            print('person ', person)

    print('length: ', len(data))

    return data

# get_category_list(999)