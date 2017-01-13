import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql
import re
import json
import time
import datetime

from mysqlmodel import Model
from mysqlmodel import Mysql

def getNowTime():
    return time.strftime("%Y=%m-%d %H:%M:%S", time.localtime(time.time()))

def filterLiveIds(url):
    html = urlopen(url)
    liveIds = set()
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.findAll("a", href=re.compile("^(/l/)")):
        if 'href' in link.attrs:
            newpage = link.attrs['href']
            liveid = re.findall("[0-9]+", newpage)
            liveIds.add(liveid[0])

    return liveIds

def getLiveIdsFromRecommendPage():
    liveds = set()
    liveids = filterLiveIds("http://www.huajiao.com/category/1000") | filterLiveIds("http://www.huajiao.com/category/1000?pageno=2")
    return liveids

def getUserId(liveId):
    html = urlopen("http://www.huajiao.com/" + "l/" + str(liveId))
    bsobj = BeautifulSoup(html, "html.parser")
    text = bsobj.title.get_text()
    res = re.findall("[0-9]+", text)
    return res[0]

def getUserData(userId):
    print("getUserData: userId="+userId)
    html = urlopen("http://www.huajiao.com/user/" + str(userId))
    bsobj = BeautifulSoup(html, "html.parser")
    data = dict()

    try:
        userinfoobj = bsobj.find("div", {"id": "userInfo"})
        data['FAvatar'] = userinfoobj.find("div", {"class": "avatar"}).img.attrs['src']
        userid = userinfoobj.find("p", {"class": "user_id"}).get_text()
        data['FUserId'] = re.findall("[0-9]+", userid)[0]
        otherattrs = userinfoobj.h3.get_text('|', strip=True).split('|')
        data['FUserName'] = otherattrs[0]
        data['FLevel'] = otherattrs[1]
        otherattrs = userinfoobj.find("ul", {"class": "clearfix"}).get_text('|', strip=True).split('|')
        data['FFollow'] = otherattrs[0]
        data['FFollowed'] = otherattrs[2]
        data['FSupported'] = otherattrs[4]
        data['FExperience'] = otherattrs[6]
        return data
    except AttributeError:
        print(str(userId) + ":html parse error in getUserData")
        return 0

