'''
第一个示例：简单的网页爬虫
爬取豆瓣首页
'''

import urllib.request
import ssl

# 网址
# url = "http://www.douban.com/"
# url = 'https://egame.qq.com/livelist?layoutid=hot'
# url = 'https://egame.qq.com/livelist?layoutid=hot&tagId=0&tagIdStr=interact_draw&tagName=%E6%8A%BD%E5%A5%96'
url = 'https://egame.qq.com/82271258'
# 请求
# context = ssl._create_unverified_context()
ssl._create_default_https_context = ssl._create_unverified_context
request = urllib.request.Request(url)

# 爬取结果
response = urllib.request.urlopen(request)

data = response.read()

# 设置解码方式
data = data.decode('utf-8')

# 打印结果
print(data)

# 打印爬取网页的各类信息

print(type(response))
print(response.geturl())
print(response.info())
print(response.getcode())
