import requests
from random import choice
from bs4 import BeautifulSoup
import time

arr = ['小米8周年,祝福小米越办越好','只希望相机能够流畅','回复不加积分了，什么时候能进miui10','您好，楼主建议等待下个版本更新看看','为什么我的内测申请还没有通过。。','羡慕能用MIUI10的','静静等待中！！着急如焚','MIUI10什么时候出稳定版啊','如何入手MIUI10?','MIUI10好用吗?','你们都是用什么版本的MIUI','内测资格在哪里申请啊?','好想用MIUI10啊','稳定版的MIUI10什么时候才能推送啊','现在的MIUI10是体验版吗?']
page = ['763','737','772','773','759','661','660','768','748','606','464','39','770','667','705']

headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
		'Cookie': 'UM_distinctid=1616efdd7843fd-0ef28e5bf93bc1-3c604504-1fa400-1616efdd785331; CNZZDATA5677709=cnzz_eid%3D1883512964-1520220348-http%253A%252F%252Fbbs.xiaomi.cn%252F%26ntime%3D1520220348; __utma=230417408.1345820426.1517985586.1524038646.1527818463.5; __utmc=230417408; __utmz=230417408.1527818463.5.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; CNZZDATA5557939=cnzz_eid%3D76633849-1517983611-null%26ntime%3D1527815291; arp_scroll_switch=1; Hm_lvt_3c5ef0d4b3098aba138e8ff4e86f1329=1527818462,1527826003; CNZZDATA30049650=cnzz_eid%3D425828580-1517982151-null%26ntime%3D1527832397; CNZZDATA2441309=cnzz_eid%3D1425032594-1517982878-null%26ntime%3D1527832792; MIUI_2132_saltkey=xqmLlGdQ; MIUI_2132_lastvisit=1527829249; MIUI_2132_visitedfid=464; MIUI_2132_auth=0977kkCbfRhH1WZnNktog8NrMAhpEJQbKyZYz772pdEnEnW%2F9OFXPQk; lastLoginTime=3c41P4o6Wen9n1rlrc76HGFsRmEjoowWunFV%2BH0qt9eh5XGpXi0d; MIUI_2132_smile=3D1; MIUI_2132_ulastactivity=38d3PAVVbPwvNyH4C79yMBOBfak8NfS0vFVNxmUl9%2FagFHG4rIlzAkk; __utmt=1; MIUI_2132_forum_lastvisit=D_464_1527834705; MIUI_2132_viewid=tid_14734505; __utmb=230417408.87.10.1527818463; Hm_lpvt_3c5ef0d4b3098aba138e8ff4e86f1329=1527834996; MIUI_2132_lastact=1527835004%09forum.php%09post; arp_scroll_position=200'
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
	soup = BeautifulSoup(get_index(url),'lxml')
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
	return res.text

for x in range(50):
	print('正在回复中...')
	p = choice(page)
	get_url('http://www.miui.com/forum-'+p+'-'+str(x)+'.html',p,choice(arr))
	time.sleep(30)
# u = 'http://www.miui.com/forum-'+p+'-'+str(1)+'.html'
# get_url(u,p,choice(arr))