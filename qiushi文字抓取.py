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
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
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

root_url="http://www.qiushibaike.com"
queue.add("http://www.qiushibaike.com/hot/")
count = 0

while queue and count < 10:
    url = queue.pop()
    visited.add(url)

    try:
        urlop = oper.open(url, timeout = 2)
        if 'html' not in urlop.getheader('Content-Type'):
            continue

        count += 1
        # 避免程序异常中止, 用try..catch处理异常

        data = urlop.read().decode('utf-8')
    except:
        continue

     # 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
    linkre = re.compile('(?<=<li>\n<a href=")(?!<).*?(?=")')
    for x in linkre.findall(data):
        if '/hot' in x and x not in visited:
            queue.add(root_url + x)
            print('%3d 加入队列 --->  %s'% (count, x))

    # 正则表达式提取页面中的内容
    linkre = re.compile('(?<=<span>)(?!<).*(?=</span>)')
    print('读取网站 --->  %s'% url)
    for x in linkre.findall(data):
        all.append(x)

f = open('d:/MyName.txt', 'w') # open for 'w'riting
while all:
    try:
        f.write(all.popleft() + '\n') # write text to file
    except:
        continue
f.close() # close the file
print('抓取结束')