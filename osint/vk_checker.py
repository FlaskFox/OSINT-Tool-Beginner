from core.colors import pink, reset  
from googlesearch import search  

class VkOSINT:
    def __init__(self, vk):
        self.vk = vk  

    def vk_checker(self):
        queries = [
            f"{self.vk}",
            f"site: vk.com {self.vk}",
            f"id{self.vk}"
        ]

        found_any = False

        for query in queries:
            print(f"\nРезультаты для запроса: {pink}{query}{reset}\n")
            results = list(search(query, num_results=15))

            if not results:
                print(f"{pink}По запросу '{query}' ничего не найдено.{reset}")
                continue

            # Фильтруем только ссылки, содержащие vk.com
            vk_links = [url for url in results if "vk.com" in url.lower()]

            if vk_links:
                found_any = True
                for url in vk_links:
                    print(url)
            else:
                print(f"{pink}Нет ссылок на vk.com по запросу '{query}'.{reset}")

        if not found_any:
            print(f"{pink}Пользователь ВК с '{self.vk}' не найден.{reset}")
