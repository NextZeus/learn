# 一步一步爬取花椒直播主播数据

## 第一步 安装所需库
* pip3 install bs4
* pip3 install requests

```
### 第二步 引入库

from bs4 import BeautifulSoup #解析HTML文件库
import requests #请求库
import re  #正则表达式库

```

### 第三步 定义通用bs4处理html文档内容方法
```
# 定义获取bs处理后的文档内容

def get_soup_by_url(url):
    html = requests.get(url)
    plain_text = html.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    return soup

```

### 第四步 定义获取直播分类的方法
```
# 获取花椒直播所有分类
def get_huajiao_video_categories():
    huajiao_main_url = "http://www.huajiao.com/"
    home_soup = get_soup_by_url(huajiao_main_url)
    #
    hd_nav = home_soup.find_all('a', {'href': re.compile('category')})
    print('hd_nav: ', hd_nav)
    categories = dict()
    for tag in hd_nav:
        des = tag.string #有两种 一种是 更多>; 另外一种是分类名
        if des == '更多>':
            continue
        print('des: ', des)
        print('name:', tag.string)
        category = tag.get('href')[10:]
        print('category: ', category)
        categories[category] = des
    print('categories:', categories)
    # 输出结果: categories: {'1000': '正在直播', '2': '女神驾到', '666': '才艺主播', '999': '校园女生', '1001': '音乐达人', '5': '娱乐明星', '1': '高清直播', '3': '高清直播'}

```

### 第五步 深入分类直播列表页面 
熬了个通宵，一晚上没睡着，撸到现在 哈哈 不过感觉撸的很爽 比平时写的要有效很多倍 可能是精力比较集中吧 接着写教程
顺便总结下bs4的一些实际经验
继续上代码

```
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
        # 这里获取的是一个嵌套的tag
        a超链接下是 2个div 一个存储主播头像地址 一个存储主播简要信息
        for link in main_list:
            person = dict()
            userId = link.get('href')[3:]
            person['userId'] = userId
            children = link.children

            for child in children:
                # 总共4个child , 有两个是NavigableString 下面要排除掉无用child
                # child是最外层两个div 
                
                if not isinstance(child, NavigableString):
                    attr = child.attrs['class'][0]
                    if attr == 'pic':
                        #头像 child.image 获取image tag
                        avatar = child.img.get('src')
                        person['avatar'] = avatar
                        # print('avatar: ', avatar)
                    elif attr == 'text':
                        # 第一个div 主播昵称 
                        # child.div 获取第一个div子节点 ; 第二个不能这么获取
                        nickName = child.div.get_text()
                        person['nickName'] = nickName
                        # 获取span里的正在观看人数
                        # 我换了一种方式获取 数据是在span标签里放着的 所以我就直接从span里拿
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

```

![](http://img.hb.aicdn.com/db803d05ce7b754d726eadbe1acb0b5afaa1dc21dba4-DcRXsZ_fw658)





