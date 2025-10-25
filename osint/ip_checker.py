# Built-in modules
from fake_useragent import UserAgent
import requests
import ipwhois

# Core/
from core.colors import pink, reset  

ua = UserAgent().random
headers = {
	"User-Agent": ua
}

""" IP OSINT class """
class IPOSINT:
	def __init__(self, ip):
		self.ip = ip  

	def ip_checker(self):
		# IP-API service
		url = f"http://ip-api.com/json/{self.ip}"
		try:
			response = requests.get(url, headers=headers)
			if response.ok:
				data = response.json()
				status = data.get("status", "неизвестно")
				country = data.get("country", "неизвестно")
				country_code = data.get("countryCode", "неизвестно")
				region = data.get("region", "неизвестно")
				region_name = data.get("regionName", "неизвестно")
				city = data.get("city", "неизвестно")
				zip_code = data.get("zip", "неизвестно")
				lat = data.get("lat", "неизвестно")
				lon = data.get("lon", "неизвестно")
				timezone = data.get("timezone", "неизвестно")
				isp = data.get("isp", "неизвестно")
				org = data.get("org", "неизвестно")
				as_s = data.get("as", "неизвестно")

				ip_results = f"""
	┌─[+] Результат поиска по сервису IP-API:
	├ Статус: {status}
	├ Cтрана: {country}
	├ Код страны: {country_code}
	├ Регион: {region}
	├ Название региона: {region_name}
	├ Город: {city}
	├ Почтовый индекс: {zip_code}
	├ Широта: {lat}
	├ Долгота: {lon}
	├ Часовой пояс: {timezone}
	├ Провайдер: {isp}
	├ Организация: {org}
	└ As: {as_s}
				"""

				print(f"{pink}{ip_results}{reset}")

			elif response.status_code == 404:
				print(f"{pink}[!] Сайт не найден, ошибка: {response.status_code}")
			else:
				print(f"{pink}[!] Сервер не работает, ошибка: {response.status_code}")

		except requests.RequestException as e:
			print(f"{pink}[!] Ошибка: {e}{reset}")

		# Ipinfo service
		url = f"https://ipinfo.io/{self.ip}/json"
		try:
			response = requests.get(url, headers=headers)
			if response.ok:
				data = response.json()
				ip = data.get("status", "неизвестно")
				city = data.get("country", "неизвестно")
				region = data.get("region", "неизвестно")
				country = data.get("country", "неизвестно")
				loc = data.get("loc", "неизвестно")
				org = data.get("org", "неизвестно")
				postal = data.get("postal", "неизвестно")
				timezone = data.get("timezone", "неизвестно")

				ip_results = f"""
	┌─[+] Результат поиска по сервису IP-API:
	├ IP: {ip}
	├ Cтрана: {country}
	├ Город: {city}
	├ Регион: {region}
	├ Локация: {loc}
	├ Организация: {org}
	├ Почтовый индекс: {postal}
	└ Часовой пояс: {timezone}
				"""

				print(f"{pink}{ip_results}{reset}")

			elif response.status_code == 404:
				print(f"{pink}[!] Сайт не найден, ошибка: {response.status_code}")
			else:
				print(f"{pink}[!] Сервер не работает, ошибка: {response.status_code}")

		except requests.RequestException as e:
			print(f"{pink}[!] Ошибка: {e}{reset}")