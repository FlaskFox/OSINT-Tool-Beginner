#!/usr/bin/env python3

from generator import Generator_fake
# Core/
from core.colors import pink, reset 
# Scanner/
from scanners.webscanner import webScanner
from scanners.xsscanner import XSScanner
# Osint/
from osint.phone_checker import PhoneOSINT
from osint.ip_checker import IPOSINT
from osint.mac_checker import MacOSINT
from osint.username_checker import UsernameOSINT
from osint.fio_checker import FIOOSINT
from osint.vk_checker import VkOSINT
# Telegram/
from telegram.module import Module 
from telegram_checker import TelegramOSINT

try:
	# Built-in modules
	import subprocess, sys, os
except ModuleNotFoundError:
	print(f"{pink}[!] Модули не найдены{reset}")
	print(f"{pink}[*] Установка необходимых зависимостей, ожидайте...{reset}")
	subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
	sys.exit(1)

""" Main class to run program """
class Base:
	def __init__(self, phone_number='', username='', ip=''):
		self.phone_number = phone_number
		self.username = username
		self.ip = ip

	def main_banner(self):
		banner = """
 ██╗  ██╗ █████╗ ██████╗ ███╗   ███╗ █████╗ 
 ██║ ██╔╝██╔══██╗██╔══██╗████╗ ████║██╔══██╗
 █████╔╝ ███████║██████╔╝██╔████╔██║███████║
 ██╔═██╗ ██╔══██║██╔═══╝ ██║╚██╔╝██║██╔══██║
 ██║  ██╗██║  ██║██║     ██║ ╚═╝ ██║██║  ██║
  ═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚═╝╚═╝  ╚═╝
                                           
Создатель: Marvin | @mvdmarvin					     
Version: v1.0										 

[1.0] Поиск по номеру     [2.0] Модуль Telegram	    [3.0] Генератор всех данных
[1.1] Поиск по никнейму   [2.1] Веб-сканер
[1.2] Поиск по IP         [2.2] Сканер XSS
[1.3] Поиск по MAС
[1.4] Поиск по ФИО
[1.5] Поиск по Telegram
[1.6] Поиск по VK
[0] Выход
		"""

		print(f"{pink} {banner} {reset}")

	def return_menu(self):
		input(f"{pink} Нажмите Enter чтобы вернуться в меню... {reset}")

	def clear_screen(self):
		os.system("cls" if os.name == "nt" else "clear")

""" Main function """
def main():
	base = Base()
	base.main_banner()
	while True:
		user_choice = input(f"{pink}[?] Выбор >>> {reset}").strip()
		if user_choice == "1.0":
			base.clear_screen()
			phone_number = input(f"{pink}[?] Введите номер телефона >>> {reset}").strip()
			phone_osint = PhoneOSINT(phone_number)
			phone_osint.phone_checker()
			base.return_menu()
			base.clear_screen()
			base.main_banner()
		elif user_choice == "1.1":
			base.clear_screen()
			username = input(f"{pink}[?] Введите никнейм >>> {reset}").strip()
			username_osint = UsernameOSINT(username)
			username_osint.username_checker()
			base.return_menu()
			base.clear_screen()
			base.main_banner()
		elif user_choice == "1.2":
			base.clear_screen()
			ip = input(f"{pink}[?] Введите IP >>> {reset}").strip()
			ip_osint = IPOSINT(ip)
			ip_osint.ip_checker()
			base.return_menu()
			base.clear_screen()
			base.main_banner()
		elif user_choice == "1.3":
			base.clear_screen()
			mac = input(f"{pink}[?] Введите MAC >>> {reset}").strip()
			mac_osint = MacOSINT(mac)
			mac_osint.mac_checker()
			base.return_menu()
			base.clear_screen()
			base.main_banner()
		elif user_choice == "1.4":
			base.clear_screen()
			fio = input(f"{pink}[?] Введите ФИО >>> {reset}").strip()
			fio_osint = FIOOSINT(fio)
			fio_osint.fio_checker()
			base.return_menu()
			base.clear_screen()
			base.main_banner()
		elif user_choice == "1.5":
			base.clear_screen()
			telegram_id = input(f"{pink}[?] Введите ID Telegram пользователя >>> {reset}").strip()
			telegram_osint = TelegramOSINT(telegram_id)
			telegram_osint.telegram_checker()
			base.return_menu()
			base.clear_screen()
			base.main_banner()
		elif user_choice == "1.6":
			base.clear_screen()
			vk_id = input(f"{pink}[?] Введите vk id пользователя >>> {reset}").strip()
			vk_osint = VkOSINT(vk_id)
			vk_osint.vk_checker()
			base.return_menu()
			base.clear_screen()
			base.main_banner()
		elif user_choice == "2.0":
			base.clear_screen()
			session_name = input(f"{pink}[?] Введите название своей сессии >>> {reset}").strip()
			api_id = input(f"{pink}[?] Введите свой API_ID >>> {reset}").strip()
			api_hash = input(f"{pink}[?] Введите свой API_HASH >>> {reset}").strip()
			module = Module(session_name, api_id, api_hash)
			module.module_start()
			base.return_menu()
			base.clear_screen()
			base.main_banner()
		elif user_choice == "2.1":
			base.clear_screen()
			url = input(f"{pink}[?] Введите URL >>> {reset}").strip()
			web_scanner = webScanner(url)
			web_scanner.site_information()
			base.return_menu()
			base.clear_screen()
			base.main_banner()
		elif user_choice == "2.2":
			base.clear_screen()
			url = input(f"{pink}[?] Введите URL >>> {reset}").strip()
			xss_scanner = XSScanner(url)
			xss_scanner.xss_run()
			base.return_menu()
			base.clear_screen()
			base.main_banner()
		elif user_choice == "3.0":
			base.clear_screen()
			generator = Generator_fake()
			generator.start_gen()
			base.return_menu()
			base.clear_screen()
			base.main_banner()

		elif user_choice == "0":
			print(f"{pink}Выход... {reset}")
		else:
			print(f"{pink}[!] Неверная команда {reset}")
			base.clear_screen()
			base.main_banner()

""" Run main """
if __name__ == "__main__":
	main()

input()