import requests  

from core.colors import pink, reset  

class UsernameOSINT:
	def __init__(self, username):
		self.username = username

	def username_checker(self):
		social_media = {
			"facebook": "https://www.facebook.com/{username}",
			"instagram": "https://www.instagram.com/{username}",
			"vk": "https://www.vk.com/{username}",
			"youtube": "https://www.youtube.com/{username}",
			"twitter": "https://twitter.com/{username}",
            "tiktok": "https://www.tiktok.com/@{username}",
            "pinterest": "https://www.pinterest.com/{username}",
            "reddit": "https://www.reddit.com/user/{username}",
            "tumblr": "https://{username}.tumblr.com",
            "soundcloud": "https://soundcloud.com/{username}",
            "github": "https://github.com/{username}",
            "medium": "https://medium.com/@{username}",
            "flickr": "https://www.flickr.com/people/{username}",
            "steam": "https://steamcommunity.com/id/{username}",
            "discord": "https://discordapp.com/users/{username}",
            "goodreads": "https://www.goodreads.com/{username}",
		}

		for key, value in social_media.items():
			full_url = value.format(username=self.username)
			response = requests.get(full_url, timeout=3, allow_redirects=True)
			if response.ok:
				print(f"{pink}[+] Аккаунт {self.username} найден на сервисе: {key}{reset}")
			elif response.status_code == 404:
				print(f"{pink}[+] Аккаунт {self.username} не найден на сервисе: {key}{reset}")
			else:
				print(f"{pink}[+] Ошибка сервера: {response.status_code}{reset}")

