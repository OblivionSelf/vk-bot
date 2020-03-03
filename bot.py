import vk_api
import random
import re
import time
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

class Bot:
	def __init__(self):
		self.vk_session = vk_api.VkApi(token='тут твой токен')
		self.vk = self.vk_session.get_api()
		self.longpoll = VkBotLongPoll(self.vk_session, 185746531)
		self.running = True
		self.main_loop()

	def message(self,message,attachment=None):
		self.randnum = random.randint(-2147483648, +2147483648)
		self.vk.messages.send(peer_id=self.peer_id,message=self.user_name + message,random_id=self.randnum,attachment=attachment)

	def main_loop(self):
		# Основной цикл бота
		print("БОТ > Успешно запущен!")
		while self.running is True:
			time.sleep(2)
			for event in self.longpoll.listen():
				if event.type == VkBotEventType.MESSAGE_NEW:
					self.response = event.obj.text.lower()
					self.peer_id = event.obj.peer_id
					self.from_id = event.obj.from_id
					self.user_name = "@id" + str(self.from_id) + " (" + str(self.vk.users.get(user_ids=self.from_id)[0]['first_name']) + "), "

					if self.peer_id != self.from_id:
						# Сообщение пришло из беседы
						if self.response == "/тест":
							self.message("привет!\nЯ SevenBot.\nСейчас я запущен и работаю.")
						if re.search("кто пися",self.response):
							self.randhum = self.vk.messages.getConversationMembers(peer_id=self.peer_id)['profiles'][0]
							self.message("вот же она - @id" + str(self.randhum['id']) + " (" + self.randhum['first_name'] + " " + self.randhum['last_name'] + ")")

# Запуск бота
if __name__ == "__main__":
	start = Bot()
