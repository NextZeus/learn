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
... 待续






