# 花椒直播爬虫

## 目标需求
* 收集huajiao.com上的人气主播信息:每位主播的关注数，粉丝数，赞数，经验值等数据
* 收集每位人气主播的直播历史数据，包括每次直播的开播时间，观看人数，赞数等数据

## 逻辑步骤
 * 直播页面url : http://www.huajiao.com/l/liveId liveId唯一标识一个直播
 * 主播个人主页：http://www.huajiao.com/user/userId userId唯一标识一个主播用户

## 程序逻辑
* 选择热门推荐 http://www.huajiao.com/category/1000
* 过滤页面所有的直播地址 http://www.huajiao.com/l/liveId
* 通过直播ID抓取直播页面的html, 并过滤出主播的userId
* 通过userId抓取主播的个人主页，过滤出关注数，粉丝数，赞数，经验值；过滤出直播历史数据
* 将用户数据和直播历史数据写入mysql保存

## 注意事项
* 爬虫定时执行，对于已经采集的数据，采取何种更新策略
* 直播历史数据需要请求响应的ajax接口， 对收到的数据进行json解码分析
* 主播昵称包含emoji表情，如果数据库使用常用的编码"utf8"则会写入报错
* 过滤直播地址来获取直播ID时，需要使用到正则匹配，使用Python库 "re"
* 分析html, 使用 BeautifulSoup
* 读写mysql 使用 pymysql

### 数据库设计
![](http://mmbiz.qpic.cn/mmbiz_png/vtJpaLUJ689NF4Ra0LXiaaGnGuABpXibvtXgW1gza4jiaiazRsZQrQyWglymtZHtfXFCe148mG9DA6Cj27OWtQfrtQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)
> Tbl_Huajiao_User用于存储主播的个人数据
> Tbl_Huajiao_Live用于存储主播的历史直播数据