from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantsBots, ChannelParticipantsAdmins
import asyncio, random, time

from core.colors import pink, reset

class Module:
	def __init__(self, session_name='', api_id='', api_hash=''):
		self.session_name = session_name
		self.api_id = api_id
		self.api_hash = api_hash
		self.client = None
		self.my_id = None
		self.spammer_active = {}

	def module_start(self):
		self.client = TelegramClient(self.session_name, self.api_id, self.api_hash)
		print(f"{pink}[+] Модуль успешно запущен{reset}")

		@self.client.on(events.NewMessage(pattern=r"\.start"))
		async def start_handler(event):
			await event.client.send_message(event.chat.id, "Бот запущен! Введите /commands чтобы увидеть все команды")
		
		@self.client.on(events.NewMessage(pattern=r'\.commands'))
		async def commands_handler(event):
			commands = """
🌘 Все команды 🌘

▪️ .start - начать работу бота 
▪️ .myinfo - информация о себе
▪️ .chatinfo - информация о группе
▪️ .spammer - запускает спам атаку под определенное сообщение
▪️ .module - запустить модуль

			"""
			await event.client.send_message(event.chat.id, commands)

		@self.client.on(events.NewMessage(pattern=r'\.myinfo'))
		async def my_info_handler(event):
			me = await event.client.get_me()
			photo = await event.client.get_profile_photos(me.id)
			total_photos = len(photo)
			if me.photo:
				await event.reply(file=photo[0])
			me_info = f"""
┌ 🆔 ID: {me.id}
├ 📧 Username: {me.username if me.username else "неизвестно"}
├ 👤 Имя: {me.first_name if me.first_name else "неизвестно"}
├ 👤 Фамилия: {me.last_name if me.last_name else "неизвестно"}
├ 🤖 Бот: {"бот" if me.bot else "не бот"}
├ 👑 Премиум: {"премиум" if me.premium else "не премиум"}
├ 🈳 Язык: {me.lang_code if me.lang_code else "неизвестно"}
├ ✅ Верифицирован: {"верифицирован" if me.verified else "не верифицирован"}
├ ❇️ Cтатус: {"онлайн" if me.status else "оффлайн"}
├ 🖼 Фотографии профиля: {total_photos}
└ 🔗 Ссылка: {'https://t.me/' + me.username if me.username else 'неизвестно'}
			"""

			await event.reply(me_info)

		@self.client.on(events.NewMessage(pattern=r'\.chatinfo'))
		async def chat_info_handler(event):
			chat = await event.get_chat()
			participants = await event.client.get_participants(chat.id)
			admins = await event.client.get_participants(chat.id, filter=ChannelParticipantsAdmins)
			bots = await event.client.get_participants(chat.id, filter=ChannelParticipantsBots)

			chat_info = f"""
О группе:

┌ 🆔 ID: {chat.id}
├ 👥 Username: {chat.username if chat.username else 'неизвестно'}
├ 👥 Участников: {len(participants)}
├ 👑 Админов: {len(admins)}
├ 🤖 Ботов: {len(bots)}
└ 🔗 Ссылка: {'https://t.me/' + chat.username if chat.username else 'нет'}
			"""

			await event.reply(chat_info)

		@self.client.on(events.NewMessage(pattern=r'\.spammer (.*)'))
		async def spammer_handler(event):
			if event.sender_id == self.my_id:
				chat_id = event.chat_id
				text_to_spam = event.pattern_match.group(1)
				if not self.spammer_active.get(chat_id, False):
					self.spammer_active[chat_id] = True
					await self.client.send_message(chat_id, '⚡️ Спамер запущен ⚡️', parse_mode='html')
					while self.spammer_active[chat_id]:
						await self.client.send_message(chat_id, text_to_spam)
						await asyncio.sleep(0.1)
				else:
					await event.reply("Спамер уже запущен в этом чате!")

		@self.client.on(events.NewMessage(pattern=r'\.spammer_stop'))
		async def spammer_stop_handler(event):
			if event.sender_id == self.my_id:
				chat_id = event.chat_id
				if self.spammer_active.get(chat_id, False):
					self.spammer_active[chat_id] = False
					await self.client.send_message(chat_id, '⚡️ Спамер остановлен! ⚡️')
				else:
					await event.reply("Спамер не запущен.")
			else:
				await event.reply("⚡️ Эта команда доступна только создателю! ⚡️")

		start_module = False
		@self.client.on(events.NewMessage(pattern=r'\.module'))
		async def module_handler(event):
			global start_module
			start_module = True
			chat_id = event.chat_id
			await event.client.send_message(chat_id, "модуль запущен")

			payloads = [
				"[🩸] Либидно сосешь [🩸]",
				"[🩸] Ты слабак [🩸]",
				"[🩸] Ты же понимаешь что я начну щас присовывать свой хуй словно нож те в глазные яблоки [🩸]",
				"[🩸] Я внатуре ща те ебло сломаю [🩸]",
				"[🩸] Ты не более чем хуесос нищий [🩸]",
				"[🩸] Я щас всуну арматуру те в очелище [🩸]",
				"[🩸] Просверлил те голову и там опарыши... [🩸]",
				"[🩸] Ты даже не пытайся дать какой нибудь отпор мне [🩸]",
				"[🩸] Ну ты внатуре ваще слабак... [🩸]",
				"[🩸] Ну сломал те еблище [🩸]",
				"[🩸] Ты уебище жирное [🩸]",
				"[🩸] Ну ломаю те еблище пока ты выписываешь свой мизер) [🩸]",
				"[🩸] Ну ты и слабый хуесос и хач дырявый [🩸]",
				"[🩸] Дай отпора хоть какого нибудь [🩸]",
				"[🩸] Ты же понимаешь что я таким как ты ломаю еблище мигом своим хуем [🩸]"
			]

			while start_module:
				random_payload = random.choice(payloads)
				await event.client.send_message(chat_id, random_payload)
				time.sleep(10)

		@self.client.on(events.NewMessage(pattern=r'\.stop_module'))
		async def stop_module_handler(event):
			global start_module
			chat_id = event.chat_id
			if start_module:
				start_module = False
				await event.client.send_message(chat_id, "Модуль остановлен!")

		async def main():
           	# Получаем свой ID при старте
			me = await self.client.get_me()
			self.my_id = me.id
			print(f"{pink}[+] Модуль успешно запущен{reset} — мой ID: {self.my_id}")

		self.client.start()
		self.client.loop.run_until_complete(main())
		self.client.run_until_disconnected()
