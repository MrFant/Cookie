# -*- coding:utf-8 -*-
import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers={'User-Agent':user_agent}
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
			'email':'15706568439',
			'password':'fy19970309'
		})

loginUrl = 'http://www.imooc.com/user/newlogin'
#模拟登录，并把cookie保存到变量
request=urllib2.Request(loginUrl,postdata,headers)
result = opener.open(request)
#保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
#利用cookie请求访问另一个网址，此网址是成绩查询网址
gradeUrl = 'http://www.imooc.com/u/4918638/notices'
#请求访问成绩查询网址
result = opener.open(request)
print result.read()
