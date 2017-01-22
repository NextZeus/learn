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
    return categories

# 根据 分类id 和 页码 获取对应请求的url
def get_category_url_by_id_and_pageno(catgory_id, pageno):
    catgory_url = "http://www.huajiao.com/category/" + str(catgory_id) + "pageno=" + str(pageno)
    return catgory_url

# 获取直播分类列表数据
def get_category_list(catgory_id):
    catgory_url = "http://www.huajiao.com/category/" + str(catgory_id)
    soup = get_soup_by_url(catgory_url)
    # 获取最大分页数
    page_tag = soup.find_all('li', "paginate_button last")
    if len(page_tag) <= 0:
        return []

    last_page_tag = soup.find_all('li', "paginate_button last")[0]
    last_page = int(last_page_tag.get('tabindex'))

    data = list()

    for pageno in range(1, last_page):
        catgory_url = get_category_url_by_id_and_pageno(catgory_id, pageno)
        soup = get_soup_by_url(catgory_url)
        main_list = soup.find_all('a', href=re.compile('/l/'))

        for link in main_list:
            person = dict()
            liveId = link.get('href')[3:]
            userid = get_anchorid_by_liveid(liveId)
            person['userid'] = userid
            children = link.children

            # todo 替换 get_anchor_info_by_userid
            # person = get_anchor_info_by_userid(userid)

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
                        span_tag = child.find_all('span', 'num')
                        if len(span_tag) <= 0:
                            watches = 0
                        else:
                            watches = child.find_all('span', 'num')[0].get_text(strip=True)
                        person['watches'] = watches
                        # print('nickName: ', nickName)
                        # print('watches: ', watches)
                    else:
                        print('continue!')
            data.append(person)
            # print('person ', person)

    # print('length: ', len(data))
    return data

# categories = get_huajiao_video_categories()
# print('花椒主播分类: ', categories)
# for category in categories.keys():
#     data = get_category_list(category)
#     print('category ' + str(category)+' anchor-number: ', len(data))

# 根据直播ID 获取主播用户ID
def get_anchorid_by_liveid(liveid):
    url = "http://www.huajiao.com/l/" + str(liveid)
    soup = get_soup_by_url(url)
    anchor_id = soup.find_all('a', href=re.compile('user/'))[0].get('href')[6:]
    return anchor_id

# 获取主播详细信息 & 直播历史纪录
def get_anchor_info_by_userid(userid):
    person = dict()

    print('userid: ', userid)
    url = "http://www.huajiao.com/user/" + str(userid)
    soup = get_soup_by_url(url)
    userInfo = soup.find_all('div', {'id': 'userInfo'})[0]

    about = userInfo.find_all('p', 'about')[0]
    person['about'] = about.get_text(strip=True)
    level = userInfo.find_all('span', 'level')[0]
    person['level'] = level.get_text(strip=True)

    clearfix = userInfo.find_all('ul', 'clearfix')[0]
    for child in clearfix.children:
        if not isinstance(child, NavigableString):
            print('child: ', child)
            p = child.find('p').get_text()
            h = child.find('h4').get_text()
            if h == '关注':
                person['follow'] = p
            elif h == '粉丝':
                person['fans'] = p
            elif h == '赞':
                person['support'] = p
            elif h == '经验值':
                person['exp'] = p

    print('person: ', person)
    return person

userid = get_anchorid_by_liveid(71956509)
get_anchor_info_by_userid(userid)