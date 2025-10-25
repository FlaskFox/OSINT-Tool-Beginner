from fake_useragent import UserAgent
import requests

from core.colors import pink, reset

ua = UserAgent().random
headers = {
	"User-Agent": ua
}

class MacOSINT:
	def __init__(self, mac):
		self.mac = mac  

	def mac_checker(self):
		# first service 
		url = f"https://api.macvendors.com/{self.mac}"
		response = requests.get(url, headers=headers)
		if response.ok:
			print(f"{pink}{response.text}{reset}")
		elif response.status_code == 404:
			print(f"{pink}[!] Сайт не найден, ошибка: {response.status_code}{reset}")
		else:
			print(f"{pink}[!] Ошибка сервера: {response.status_code}{reset}")

		# second service
		url = f"https://api.macaddresslookup.app/{self.mac}"
		response = requests.get(url, headers=headers)
		if response.ok:
			data = response.json()
			data_list = data[0]

			starthex = data_list.get("startHex", "неизвестно")
			endhex = data_list.get("endHex", "неизвестно")
			startdec = data_list.get("startDec", "неизвестно")
			company = data_list.get("company", "неизвестно")
			addressl1 = data_list.get("addressL1", "неизвестно")
			addressl2 = data_list.get("addressL2", "неизвестно")
			addressl3 = data_list.get("addressL3", "неизвестно")
			country = data_list.get("country", "неизвестно")
			type_e = data_list.get("type", "неизвестно")

			mac_results = f"""
starthex: {starthex}
endhex: {endhex}
startdec: {startdec}
company: {company}
addressl1: {addressl1}
addressl2: {addressl2}
addressl3: {addressl3}
Страна: {country}
Тип: {type_e}
			"""

			print(f"{pink}{mac_results}{reset}")
		
		elif response.status_code == 404:
			print(f"{pink}[!] Сайт не найден, ошибка: {response.status_code}{reset}")
		else:
			print(f"{pink}[!] Ошибка сервера: {response.status_code}{reset}")