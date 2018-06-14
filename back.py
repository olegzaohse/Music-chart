import vk_api
import time
import random
from settings import botlogin, botpassword, my_id

vk = vk_api.VkApi(login=botlogin, password=botpassword)
vk.auth()
values = {'out': 0, 'count': 100, 'time_offset': 60}
num = '456239'
vk.method('messages.get', values)




def w_mes(user_id, s):
	vk.method('messages.send', {'user_id': user_id, 'message': s})


def music_mes(user_id, attachment):
	vk.method('messages.send', {'user_id': user_id, 'attachment': attachment})
def get_test(user_id,s):


def random_song():
	part = random.randint(1, 2)
	if part == 1:
		song_num = random.randint(17, 99)
		song_code = '0' + str(song_num)
	else:
		song_num = random.randint(100, 177)
		song_code = str(song_num)
	return song_code




while True:
	response = vk.method('messages.get', values)
	if response['items']:
		values['last_message_id'] = response['items'][0]['id']
	for item in response['items']:
		if response['items'][0]['body'] == ('Привет'):
			w_mes(item['user_id'],
				  'Привет\n Меня зовут Music Chart bot\n Напиши (Инфо) если хочешь узнать мои возможности!')
		elif response['items'][0]['body'] == ('Инфо'):
			w_mes(item['user_id'],
				  'Вы можете выбрать ключевые команды:\n (01) Музыкальные альбомы\n  (02) Случайная песня\n  (03) Песни по жанрам')
		elif response['items'][0]['body'] == '01':
			random_pic()
			music_mes(item['user_id'], 'photo' + my_id + '_' + num '0'+ str(random.randint(17,51)))

			
		elif response['items'][0]['body'] == '02':
			random_song()
			music_mes(item['user_id'], 'audio' + my_id + '_' + num + random_song())
		elif response['items'][0]['body'] == '03':
			w_mes(item['user_id'],
				  'Выберите жанр музыки:\n(31)Поп\n(32)Хип-хоп\n(33)Рок\n (34)Тяжёлый рок\n(35)Альтернатива\n(36)Джаз\n(37)Русский реп\n(38)Русский рок\n Напишите код жанра')
		elif response['items'][0]['body'] == '31':
			song_j = random.randint(157,177)
			song_id = str(song_j)
			music_mes(item['user_id'], 'audio' + my_id + '_' + num + song_id)
		elif response['items'][0]['body'] == '32':
			song_j = random.randint(137, 156)
			song_id = str(song_j)
			music_mes(item['user_id'], 'audio' + my_id + '_' + num + song_id)
		elif response['items'][0]['body'] == '33':
			song_j = random.randint(117, 136)
			song_id = str(song_j)
			music_mes(item['user_id'], 'audio' + my_id + '_' + num + song_id)
		elif response['items'][0]['body'] == '34':
			song_j = random.randint(97, 116)
			if song_j>99:
				song_id = str(song_j)
			else:
				song_id = '0'+str(song_j)
			music_mes(item['user_id'], 'audio' + my_id + '_' + num + song_id)
		elif response['items'][0]['body'] == '35':
			song_j = random.randint(77, 96)
			song_id = '0' + str(song_j)
			music_mes(item['user_id'], 'audio' + my_id + '_' + num + song_id)
		elif response['items'][0]['body'] == '36':
			song_j = random.randint(57, 76)
			song_id = '0' + str(song_j)
			music_mes(item['user_id'], 'audio' + my_id + '_' + num + song_id)
		elif response['items'][0]['body'] == '37':
			song_j = random.randint(37, 56)
			song_id = '0' + str(song_j)
			music_mes(item['user_id'], 'audio' + my_id + '_' + num + song_id)
		elif response['items'][0]['body'] == '38':
			song_j = random.randint(17, 36)
			song_id = '0' + str(song_j)
			music_mes(item['user_id'], 'audio' + my_id + '_' + num + song_id)



	time.sleep(1)