import requests
import json
import random
from bs4 import BeautifulSoup
import time

# 回复的板块id
# # 61软件 62游戏 63壁纸 41主题
circleId = ['61','62','63','41']
# 回复的内容
content = ['好东西大家一起玩','不错的资源,谢谢分享。。。。。。','这东西可以玩玩','回帖是一种美德，顶贴是给楼主热心分享的动力！！！各位机油认真回复','真的吗，我来看看','真的那么神奇吗','看看能不能打开','一定要试试看，好不好用。','是不是真的啊大兄弟老铁666','厉害,可以,666','MIUI 因你更精彩!','Good，感谢分享~','辛苦了，后排支持一下！！！','赞一个,好东西!','感谢你的分享 ，期待分享更多给力资源！','顶。。。。。。。。。。。。。。。。','感觉分享!!!','支持一下!!!','不错 支持一下','好东西,先谢谢了','谢谢分享，有你精彩！','谢谢楼主分享']
# 请求头和cookie
headers = {
	'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 8.0.0; MIX 2 MIUI/8.6.13)',
	'Cookie':''
}

# 获取列表
def get_list(circleId):
	circleId = str(circleId)
	page = str(random.randint(1,10))
	try:
		# 获取资源
		res = requests.get('https://api.bbs.miui.com/app/circle/circledisplay?circleId='+circleId+'&page='+page,headers=headers)
		# 获取0到19的随机数
		num = random.randint(0,19)
		if res.status_code == 200:
			text = json.loads(res.text)
			# 返回随机id
			return text['list'][num]['id']
		return None
	except Exception as e:
		return None

# 发送回复
def  send(tid):
	# 模拟回复接口
	params = {
		'attachnew':'',
		'fromClient':'chiron',
		'message':random.choice(content),
		'tid':tid
	}
	res = requests.post('https://api.bbs.miui.com/app/forum/reply',headers=headers,params=params)
	return json.loads(res.text)

success = 0
error = 0
while True:
	res = send(get_list(random.choice(circleId)))
	if res['error'] == 0:
		success += 1
	else:
		error += 1
		print(res['desc'])
	print('成功:%s次  失败:%s次' %(success,error))
	time.sleep(20)
