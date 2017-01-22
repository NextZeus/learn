from bs4 import BeautifulSoup
import re
import requests

url = ""
html = requests.get(url)
plain_text = html.text
soup = BeautifulSoup(plain_text, 'html.parser')

# <html>
#  <head>
#   <title>
#    The Dormouse's story
#   </title>
#  </head>
#  <body>
#   <p class="title">
#    <b>
#     The Dormouse's story
#    </b>
#   </p>
#   <p class="story">
#    Once upon a time there were three little sisters; and their names were
#    <a class="sister" href="http://example.com/elsie" id="link1">
#     Elsie
#    </a>
#    ,
#    <a class="sister" href="http://example.com/lacie" id="link2">
#     Lacie
#    </a>
#    and
#    <a class="sister" href="http://example.com/tillie" id="link3">
#     Tillie
#    </a>
#    ; and they lived at the bottom of a well.
#   </p>
#   <p class="story">
#    ...
#   </p>
#  </body>
# </html>
soup.title
# <title>The Dormouse's story</title>

soup.title.name
# u'title'

soup.title.string
# u'The Dormouse's story'

soup.title.parent.name
# u'head'

soup.p
# <p class="title"><b>The Dormouse's story</b></p>

soup.p['class']
# u'title'

soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find(id="link3")
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

# 从文档中找到所有<a>标签的链接:
for link in soup.find_all('a'):
    print(link.get('href'))

# 从文档中获取所有文字内容:
soup.get_text()


#tag.name
#属性 tag['class'] tag.class ; del tag.id

# 最常见的多值的属性是 class (一个tag可以有多个CSS的class). 还有一些属性 rel , rev , accept-charset , headers , accesskey . 在Beautiful Soup中多值属性的返回类型是list
#multi attributes
css_soup = BeautifulSoup('<p class="body strikeout"></p>')
css_soup.p['class']
# ["body", "strikeout"]

css_soup = BeautifulSoup('<p class="body"></p>')
css_soup.p['class']
# ["body"]

# 如果某个属性看起来好像有多个值,但在任何版本的HTML定义中都没有被定义为多值属性,那么Beautiful Soup会将这个属性作为字符串返回
# id 没有被定义为多值属性
id_soup = BeautifulSoup('<p id="my id"></p>')
id_soup.p['id']
# 'my id'

# tag中包含的字符串不能编辑,但是可以被替换成其它的字符串,用 replace_with() 方法:
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b
tag.string.replace_with("No longer bold")
tag
# <blockquote>No longer bold</blockquote>
soup.body.b # 获取第一个标签

# tag的contents属性 可以将tag的字节点以列表的方式输出
# children 属性 对字节点进行循环



# strings stripped_strings
# 如果tag中包含多个字符串 [2] ,可以使用 .strings 来循环获取:

for string in soup.strings:
    print(repr(string))
    # u"The Dormouse's story"
    # u'\n\n'
    # u"The Dormouse's story"
    # u'\n\n'
    # u'Once upon a time there were three little sisters; and their names were\n'
    # u'Elsie'
    # u',\n'
    # u'Lacie'
    # u' and\n'
    # u'Tillie'
    # u';\nand they lived at the bottom of a well.'
    # u'\n\n'
    # u'...'
    # u'\n'

# 输出的字符串中可能包含了很多空格或空行, 使用.stripped_strings
# 可以去除多余空白内容:

for string in soup.stripped_strings:
    print(repr(string))
    # u"The Dormouse's story"
    # u"The Dormouse's story"
    # u'Once upon a time there were three little sisters; and their names were'
    # u'Elsie'
    # u','
    # u'Lacie'
    # u'and'
    # u'Tillie'
    # u';\nand they lived at the bottom of a well.'
    # u'...'

#.next_sibling 和 .previous_sibling兄弟节点

# .next_element .previous_element

# 搜索文档树
# find() find_all()

html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc)

#字符串
soup.find_all('b')

#正则表达式
soup.find_all(re.compile('^b'))

#列表 返回所有符合标签的内容
soup.find_all(['a', 'b'])

# True 返回所有的标签
soup.find_all(True)

# 过滤器方法

def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

soup.find_all(has_class_but_no_id())


#find_all
soup.find_all('title')

soup.find_all('p', 'title') #class='title'

# keyword 参数
soup.find_all(id="link2")
soup.find_all(text=re.compile('sister'))
# 字典参数
soup.find_all(attrs={"data-foo": "value"})

# 按css 搜索
soup.find_all('a', class_='sister')
soup.find_all(class_=re.compile('itl'))

def has_six_characters(css_class):
    return css_class is not None and len(css_class) == 6

soup.find_all(class_=has_six_characters)

# 多值属性
# 完全匹配 class 的值时,如果CSS类名的顺序与实际不符,将搜索不到结果
css_soup.find_all("p", class_="body strikeout")

soup.find_all("a", attrs={"class": "sister"})

# text 参数
# 通过 text 参数可以搜搜文档中的字符串内容

# limit 参数

#去除文档前后空白
soup.get_text("|", strip=True)
