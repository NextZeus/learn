# filter out live ids from a url
def filterLiveIds(url):
    html = urlopen(url)
    liveIds = set()
    bsObj = BeautifulSoup(html, "html.parser")
    