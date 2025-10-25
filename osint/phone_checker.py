# Built-in modules
from phonenumbers import carrier, timezone, geocoder, format_number, PhoneNumberFormat, PhoneNumberType
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from datetime import datetime
import pytz
import requests
import json
import phonenumbers
import webbrowser

# Core/
from core.colors import pink, reset  

# Headers
ua = UserAgent().random
headers = {
	"User-Agent": ua
}

""" Phone OSINT class """
class PhoneOSINT:
	def __init__(self, phone_number):
		self.phone_number = phone_number

	def phone_checker(self):
		try:
			parsed_number = phonenumbers.parse(self.phone_number, None)
			# Validity number
			is_valid = phonenumbers.is_valid_number(parsed_number)
			is_possible = phonenumbers.is_possible_number(parsed_number)

			# Phone information
			country_code = parsed_number.country_code
			region_code = phonenumbers.region_code_for_number(parsed_number)
			carrier_number = carrier.name_for_number(parsed_number, 'ru')
			geocoder_number = geocoder.description_for_number(parsed_number, 'ru')
			timezone_number = timezone.time_zones_for_number(parsed_number)
			
			# Phone formats checker
			national = phonenumbers.format_number(parsed_number, PhoneNumberFormat.NATIONAL)
			international = phonenumbers.format_number(parsed_number, PhoneNumberFormat.INTERNATIONAL)
			e164 = phonenumbers.format_number(parsed_number, PhoneNumberFormat.E164)
			rfc3966 = phonenumbers.format_number(parsed_number, PhoneNumberFormat.RFC3966)

			# Phone time
			tz_info = timezone_number[0] if timezone_number else None
			local_time = datetime.now(pytz.timezone(tz_info)).strftime("%Y-%m-%d %H:%M:%S") if tz_info else 'неизвестно'

			# Phone type checker
			number_type = phonenumbers.number_type(parsed_number)
			type_map = {
                PhoneNumberType.MOBILE: "Мобильный номер",
                PhoneNumberType.FIXED_LINE: "Фиксированный номер",
                PhoneNumberType.TOLL_FREE: "Бесплатный номер",
                PhoneNumberType.PREMIUM_RATE: "Премиум номер",
                PhoneNumberType.SHARED_COST: "Номер с разделенной стоимостью",
                PhoneNumberType.VOIP: "VoIP номер",
                PhoneNumberType.PERSONAL_NUMBER: "Персональный номер",
                PhoneNumberType.PAGER: "Пейджер",
                PhoneNumberType.UAN: "UAN номер",
                PhoneNumberType.VOICEMAIL: "Голосовая почта"
            }
			
			number_type_description = type_map.get(number_type, "Неизвестный тип номера")

			phone_results = f"""
┌─[+] Базовая информация
│
├─[+] Валидность номера
├ Верный: {'верный' if is_possible else 'неверный'}
├ Валидный: {'валидный' if is_valid else 'невалидный'}
│
├─[+] Форматы номера
├ Национальный: {national}
├ Международный: {international}
├ E164: {e164}
├ RFC3966: {rfc3966}
│
├─[+] Основная информация
├ Код страны: {country_code}
├ Код номера: {region_code}
├ Страна: {geocoder_number or 'неизвестен'}
├ Оператор: {carrier_number or 'неизвестен'}
├ Часовой пояс: {timezone_number or 'неизвестен'}
├ Местное время: {local_time}
│
├─[+] Ручная проверка (Проверьте номер в следующих ресурсах)
│
├─[+] Мессенджеры
├ Whatsapp: https://wa.me/{self.phone_number}
├ Telegram: https://t.me/{self.phone_number}
├ Viber: viber://add?number={self.phone_number}
├ Skype звонок: skype:{self.phone_number}?call
│
├─[+] Специальные сервисы
├ Truecaller: https://www.truecaller.com/search/{country_code}/{self.phone_number}
├ Numverify: https://numverify.com/results?number={self.phone_number}
│
├─[+] Соцсети
├ Facebook: https://www.facebook.com/login/identify/
├ Instagram: https://www.instagram.com/accounts/password/reset/
├ Twitter: https://x.com/i/flow/password_reset
├ Vk: "https://vk.com/restore
├ Ok: https://ok.ru/dk?st.cmd=anonymRecoveryStartPhoneLink 
├ Linkedin: https://www.linkedin.com/checkpoint/rp/request-password-reset?trk=guest_homepage-basic_nav-header-signin
├ Reddit: https://www.reddit.com/password/
├ 
├─[+] Поисковые системы
├ Google: https://www.google.com/search?q={self.phone_number}
├ Yandex: https://yandex.ru/search/?text={self.phone_number} 
├ Yahoo: https://search.yahoo.com/search?p={self.phone_number} 
├ Bing: https://www.bing.com/search?q={self.phone_number} 
├ Mail.ru: https://mail.ru/search?text={self.phone_number} 
├ DuckDuckGo: https://duckduckgo.com/?t=h_&q={self.phone_number} 
├ Onion Engine: https://onionengine.com/msearch.php?search={self.phone_number} 
├ Aol: https://search.aol.com/aol/search?q={self.phone_number} 
├ Qwant: https://www.qwant.com/?q={self.phone_number} 
├ Startpage: https://www.startpage.com/search?q={self.phone_number} 
├ Brawsearch: https://search.brave.com/search?q={self.phone_number} 
└ Ask: https://www.ask.com/web?q={self.phone_number} 

           	"""

			print(f"{pink}{phone_results}{reset}")

        	# Fincalculator service
			url = f"https://fincalculator.ru/api/tel/{e164}"
			try:
				response = requests.get(url, headers=headers)
				if response.ok:
					data = response.json()
					phone = data.get('phone', 'неизвестно')
					country = data.get('country', 'неизвестно')
					region = data.get('region', 'неизвестно')
					sub_region = data.get('subRegion', 'неизвестно')
					locality = data.get('locality', 'неизвестно')
					operator = data.get('operator', 'неизвестно')
					time_zone = data.get('timeZone', 'неизвестно')
					fincalc_info = f"""
┌─[+] Результат поиска по сервису Fincalculator:
├ Номер: {phone}
├ Оператор: {operator}
├ Страна: {country}
├ Регион: {region}
├ ПодРегион: {sub_region}
├ Местность: {locality}
└ Часовой пояс: {time_zone}
					"""
					print(f"{pink}{fincalc_info}{reset}")
				elif response.status_code == 404:
					print(f"{pink}[!] Сайт недоступен{reset}")
				else:
					print(f"{pink}[!] Ошибка сервера: {response.status_code}{reset}")
			except requests.RequestException:
				print(f"{pink}[!] Ошибка: {e}{reset}")

			
			# Phoneradar service
			url = f"https://phoneradar.ru/phone/{e164}"
			try:	
				response = requests.get(url, headers=headers)
				if response.ok:
					soup = BeautifulSoup(response.text, 'html.parser')
					table = soup.find_all("table", class_="table")
					if not table:
						print(f"{pink}[!] Не найден:{reset}")
					for tab in table:
						text = tab.get_text(strip=True, separator='\n')
						print(f'{pink}├ {text}{reset}')
				elif response.status_code == 404:
					print(f"{pink}[!] Сайт недоступен{reset}")
				else:
					print(f"{pink}[!] Ошибка сервера: {response.status_code}{reset}")
			except requests.RequestException:
				print(f"{pink}[!] Ошибка: {e}{reset}")

			except phonenumbers.NumberParseException as e:
				print(f"{pink}[!] Ошибка номера: {e}{reset}")

			# HTMLWEB service
			url = f"https://htmlweb.ru/geo/api.php?json&telcod={e164}"
			try:	
				response = requests.get(url, headers=headers)
				if response.ok:
					data = response.json()
					cache = 'phonenumberinfo.json'
					zero = data.get('0', 'не найдено')
					country = data.get('country', 'не найдено')
					region = data.get('region', 'не найдено')
					capital = data.get('capital', 'не найдено') 

					if isinstance(zero, dict):
						phone_number_info = '\n┌─[+] Результаты поиска на сервисе htmlweb , ваш лимит 20 запросов:'
						phone_number_info += ' ├ Информация ID:\n'
						phone_number_info += f'├ ID: {zero.get("id", "не найдено")}\n'
						phone_number_info += f'├ Название: {zero.get("name", "не найдено")}\n'
						phone_number_info += f'├ Площадь: {zero.get("area", "не найдено")}\n'
						phone_number_info += f'├ Telcode: {zero.get("telcode", "не найдено")}\n'
						phone_number_info += f'├ Широта: {zero.get("latitude", 'не найдено')}\n'
						phone_number_info += f'├ Долгота: {zero.get("longitude", "не найдено")}\n'
						phone_number_info += f'├ Часовой пояс: {zero.get('tz', "не найдено")}\n'
						phone_number_info += f'├ ENG: {zero.get("english", "не найдено")}\n'
						phone_number_info += f'├ POST: {zero.get("post", "не найдено")}\n'
						phone_number_info += f'├ Страна: {zero.get("country", "не найдено")}\n'
						phone_number_info += f'├ POST: {zero.get("post", "не найдено")}\n'
						phone_number_info += f'├ Оператор: {zero.get("oper", "не найдено")}\n'
						phone_number_info += f'└ Мобильный номер: {zero.get("mobile", "не найдено")}\n'

						phone_number_info += '\nИнформация Страна:\n\n'
						phone_number_info += f'┌ Страна: {country.get("name", "не найдено")}\n'
						phone_number_info += f'├ Полное название: {country.get("full_name", "не найдено")}\n'
						phone_number_info += f'├ ENG: {country.get("english", "не найдено")}\n'
						phone_number_info += f'├ ISO: {country.get("iso", "не найдено")}\n'
						phone_number_info += f'├ Локация: {country.get("location", "не найдено")}\n'
						phone_number_info += f'└ Язык: {country.get("lang", "не найдено")}\n'

						phone_number_info += '\nИнформация Регион:\n\n'
						phone_number_info += f'┌ Регион: {region.get("name", "не найдено")}\n'
						phone_number_info += f'├ Округ: {region.get("okrug", "не найдено")}\n'
						phone_number_info += f'├ Автокод: {region.get("autocode", "не найдено")}\n'
						phone_number_info += f'├ ENG: {region.get("english", "не найдено")}\n'
						phone_number_info += f'└ ISO: {region.get("iso", "не найдено")}\n'

						phone_number_info += '\nИнформация Общее:\n'
						phone_number_info += f'┌ Округ: {data.get("okrug", "не найдено")}\n'
						phone_number_info += f'├ Полное название: {data.get("full_name", "не найдено")}\n'
						phone_number_info += f'├ Код страны: {data.get("country_telcod", "не найдено")}\n'
						phone_number_info += f'├ Локация: {data.get("location", "не найдено")}\n'
						phone_number_info += f'├ Столица: {capital.get("name", "не найдено")}\n'
						phone_number_info += f'├ Широта: {capital.get("latitude", "не найдено")}\n'
						phone_number_info += f'├ Долгота: {capital.get("longitude", "не найдено")}\n'
						phone_number_info += f'├ Часовой пояс: {capital.get("tz", "не найдено")}\n'
						phone_number_info += f'└ Wiki: {capital.get("wiki", "не найдено")}\n'

						print(f"{pink}{phone_number_info}{reset}")
						if data.get('status_error'):
							print(f'{pink}[!] Не удалось получить доступ к сервису{reset}')

						if data.get('limit') == 0:
							print(f'{pink}[!] Лимит окончен{reset}')

						try:
							with open(cache, 'w') as file:
								json.dump(cache, file, indent=4, ensure_ascii=False)
						except FileNotFoundError as e:
							print(f'{pink}[!] Не удалось найти файл{reset}')
				elif response.status_code == 404:
					print(f"{pink}[!] Сайт недоступен{reset}")
				else:
					print(f"{pink}[!] Ошибка сервера: {response.status_code}{reset}")
			except requests.RequestException:
				print(f"{pink}[!] Ошибка: {e}{reset}")

			except phonenumbers.NumberParseException as e:
				print(f"{pink}[!] Ошибка номера: {e}{reset}")

			
		except Exception as e:
			print(f"{pink}[!] Ошибка: {e}{reset}")

		