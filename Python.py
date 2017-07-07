import re
import urllib.request
import urllib
import http.cookiejar

from collections import deque

queue = set() #创建一个队列，存放要抓取的URL
all = deque() #创建一个队列，存放抓取到的内容
visited = set() #创建一个集合，存放已经遍历过的URL

#请求网页时添加Head
def makeMyOpener(head = {
    'Accept':' */*',
    'Accept-Encoding':' gzip, deflate, br',
    'Accept-Language':' zh-CN,zh;q=0.8',
    'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'X-Requested-With':' XMLHttpRequest'
}):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

oper = makeMyOpener()

url = "https://www.zhihu.com/login/phone_num"
count = 0

postDic = {
    '_xsrf':'4fa0e9d93d2a260476b724809332f547',
    'password':'zhang...',
    'captcha_type':'cn',
    'phone_num':'13677795610',
}

urlop = oper.open(url, urllib.parse.urlencode(postDic).encode())

data = urlop.read().decode('utf-8')

url="https://www.zhihu.com/"
urlop = oper.open(url, urllib.parse.urlencode(postDic).encode())
data = urlop.read().decode('utf-8')

print('抓取结束')