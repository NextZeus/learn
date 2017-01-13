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
    liveids = set()
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

def getUserLives(userId):
    print('getUserLives: userId=' + str(userId))

    try:
        url = "http://webh.huajiao.com/User/getUserFeeds?fmt=json&uid=" + str(userId)
        html = urlopen(url).read().decode('utf-8')
        jsondata = json.loads(html)

        if jsondata['error'] != 0:
            print(str(userId) + "error occured in getUserFeeds for: " + jsondata['msg'])
            return 0

        return jsondata['data']['feeds']
    except Exception as e:
        print('getUserData Exception:' + e)
        return 0

def getTimestamp():
    return (time.mktime(datetime.datetime.now().timetuple()))

def replaceUserLive(data):
    try:
        kvs = dict()
        kvs['FLiveId'] = int(data['relateid'])
        kvs['FUserId'] = int(data['FUserId'])
        kvs['FWatches'] = int(data['watches'])
        kvs['FPraises'] = int(data['praises'])
        kvs['FReposts'] = int(data['reposts'])
        kvs['FReplies'] = int(data['replies'])
        kvs['FPublishTimestamp'] = int(data['publishtimestamp'])
        kvs['FTitle'] = data['title']
        kvs['FImage'] = data['image']
        kvs['FLocation'] = data['location']
        kvs['FScrapedTime'] = getNowTime()
        Live().insert(kvs, 1)
    except pymysql.err.InternalError as e:
        print(e)

def spiderUserDatas():
    for liveId in getLiveIdsFromRecommendPage():
        userid = getUserId(liveId)
        userdata = getUserData(userid)
        try:
            if userdata:
                User().insert(userdata, 1)
        except pymysql.err.InternalError as e:
            print(e)
            print(userdata)
    return 1

def spiderUserLives():
    userIds = User().select("FUserId").limit(100).fetch_all()
    for userId in userIds:
        liveDatas = getUserLives(userId[0])
        try:
            for liveData in liveDatas:
                liveData['feed']['FUserId'] = userId[0]
                replaceUserLive(liveData['feed'])
        except Exception as e:
            print(e)

    return 1

class BaseModel(Model):
    conn = Mysql(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', password='123456', db='wanghong', charset='utf8')

class User(BaseModel):
    tbl = "Tbl_Huajiao_User"


class Live(BaseModel):
    tbl = "Tbl_Huajiao_Live"

