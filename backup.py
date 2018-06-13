import vk_api
import time
from settings import botlogin, botpassword
vk= vk_api.VkApi(login = botlogin , password = botpassword  )
vk.auth()
values = {'out':0, 'count':100, 'time_offset': 60 }

vk.method ('messages.get', values)

def w_mes(user_id,s):
	vk.method ('messages.send',{'user_id':user_id, 'message':s})

while True:
	response = vk.method('messages.get', values)
	if response['items']:
		values['last_message_id'] = response['items'][0]['id']
	for item in response ['items']:
			if response['items'][0]['body']=='Привет':
				w_mes(item['user_id'],
					  'Привет\n Меня зовут Music Chart bot, Напиши (инфо) если хочешь узнать мои возможности!')
			elif response ['items'][0]['body']=='инфо':
				w_mes(item['user_id'],
					  'Вы можете выбрать ключевые команды (01) музыкальный тест или (02) случайная песня или (03) песни по жанрам')
	time.sleep(1)
