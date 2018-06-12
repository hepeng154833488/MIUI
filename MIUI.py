import requests
from random import choice
from bs4 import BeautifulSoup
import time

# arr = ['小米8周年,祝福小米越办越好','只希望相机能够流畅','回复不加积分了，什么时候能进miui10','您好，楼主建议等待下个版本更新看看','为什么我的内测申请还没有通过。。','羡慕能用MIUI10的','静静等待中！！着急如焚','MIUI10什么时候出稳定版啊','如何入手MIUI10?','MIUI10好用吗?','你们都是用什么版本的MIUI','内测资格在哪里申请啊?','好想用MIUI10啊','稳定版的MIUI10什么时候才能推送啊','现在的MIUI10是体验版吗?','能否帮忙点个赞,还差点分就进内测组了.','小米MIUI10系统就是强大快更新吧','此生不悔入小米,为了进内测组,兄弟姐妹门帮忙点个赞再走呗.']
arr = ['','感谢你的分享 ，期待分享更多给力资源！','顶。。。。。。。。。。。。。。。。','感觉分享!!!','支持一下!!!','不错 支持一下','好东西,先谢谢了','谢谢分享，有你精彩！','谢谢楼主分享']
page = ['577','578','150']
# page = ['763','737','772','773','759','661','660','768','748','606','464','39','770','667','705']

headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
		'Cookie': ''
	}

def get_index(url):
	try:
		res = requests.get(url,headers=headers)
		if res.status_code == 200:
			return res.text
		return None
	except Exception as e:
		return None

def get_url(url,p,message):
	soup = BeautifulSoup(get_index(url),'html.parser')
	res = soup.select('.xst')
	get_msg(choice(res)['href'].split('-')[1],p,message)

def get_msg(tid,p,message):
	params = {
		'formhash':'0354cc54',
		'handlekey':'reply',
		'noticeauthor':'',
		'noticetrimstr':'',
		'noticeauthormsg':'',
		'usesig':1,
		'ubbject':'',
		'message':message
	}
	res = requests.post('http://www.miui.com/forum.php?mod=post&infloat=yes&action=reply&fid='+str(p)+'&extra=&tid='+str(tid)+'&replysubmit=yes&inajax=1',headers=headers,params=params)
	return res
print('正在自动回复中...')
x = 1
while True:
	if x>=50:
		x=1
	p = choice(page)
	get_url('http://www.miui.com/forum-'+p+'-'+str(x)+'.html',p,choice(arr))
	x = x+1
	time.sleep(30)
print('完成')
