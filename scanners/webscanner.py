from bs4 import BeautifulSoup
from urllib.parse import urlparse
from requests.exceptions import SSLError
import requests  
import builtwith
import socket
import ipwhois
import whois

from core.colors import pink, reset 

class webScanner:
    def __init__(self, url, domain=''):
        self.url = url
        self.domain = domain

    def site_information(self):
        domain = self.url.replace("http://", "").replace("https://", "")
        try:
            response = requests.get(self.url)
            print(f'{pink}Сертификат валиден{reset}')

            print(f"{pink}Заголовки сайта{reset}")
            for key, value in response.headers.items():
                print(f"{pink}{key}: {value}{reset}")

            print()
            print(f"{pink}Разбор URL{reset}")
            parsed_url = urlparse(self.url)
            print(f"{pink}Scheme: {parsed_url.scheme or 'не найден'}{reset}")
            print(f"{pink}Netloc: {parsed_url.netloc or 'не найден'}{reset}")
            print(f"{pink}Путь: {parsed_url.path or 'не найден'}{reset}")
            print(f"{pink}Параметры: {parsed_url.params or 'не найден'}{reset}")
            print(f"{pink}Запрос: {parsed_url.query or 'не найден'}{reset}")
            print(f"{pink}Фрагмент: {parsed_url.fragment or 'не найден'}{reset}")
            print(f"{pink}Никнейм: {parsed_url.username or 'не найден'}{reset}")
            print(f"{pink}Пароль: {parsed_url.password or 'не найден'}{reset}")
            print(f"{pink}Название хоста: {parsed_url.hostname or 'не найден'}{reset}")
            print(f"{pink}Порт: {parsed_url.port or 'не найден'}{reset}")

            ip = socket.gethostbyname(domain)
            print(f"{pink}IP сайта: {ip}{reset}")
            print(f"{pink}Информация по IP{reset}")
            ip_whois = IPWhois(ip)
            print(f"{pink}ip_whois{reset}")

            # Инициализируем переменные с дефолтными значениями
            status = "неизвестно"
            country = "неизвестно"
            country_code = "неизвестно"
            region = "неизвестно"
            region_name = "неизвестно"
            city = "неизвестно"
            zip_code = "неизвестно"
            lat = "неизвестно"
            lon = "неизвестно"
            timezone = "неизвестно"
            isp = "неизвестно"
            org = "неизвестно"
            as_s = "неизвестно"

            response_ip = requests.get(f"https://ip-api.com/json/{ip}")
            if response_ip.status_code == 200:
                try:
                    data = response_ip.json()
                    status = data.get("status", status)
                    country = data.get("country", country)
                    country_code = data.get("countryCode", country_code)
                    region = data.get("region", region)
                    region_name = data.get("regionName", region_name)
                    city = data.get("city", city)
                    zip_code = data.get("zip", zip_code)
                    lat = data.get("lat", lat)
                    lon = data.get("lon", lon)
                    timezone = data.get("timezone", timezone)
                    isp = data.get("isp", isp)
                    org = data.get("org", org)
                    as_s = data.get("as", as_s)
                except Exception:
                    print(f"{pink}[!] Не удалось распарсить JSON от IP-API{reset}")
            else:
                print(f"{pink}[!] Запрос к IP-API завершился с кодом {response_ip.status_code}{reset}")

            ip_info = f"""
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
            print(f"{pink}{ip_info}{reset}")

            print(f"{pink}Информация по IP{reset}")
            ip_whois = IPWhois(ip)
            print(f"{pink}{ip_whois}{reset}")

            print(f"{pink}Сканируем порты...{reset}")
            start_port = 1
            end_port = 1000
            open_ports = []
            for port in range(start_port, end_port + 1):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex((domain, port))
                sock.close()

                if result == 0:
                    print(f"{pink}Port: {port} открыт{reset}")
                    open_ports.append(port)

            print(f'{pink}Открытые порты: {open_ports}{reset}')


        except SSLError:
            print(f"{pink}[!] Сертификат не валиден{reset}")
        except Exception as e:
            print(f"{pink}[!] Ошибка: {e}{reset}")
