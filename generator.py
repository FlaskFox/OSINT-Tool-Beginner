from core.colors import pink, reset
from faker import Faker

from core.colors import pink, reset

fake = Faker('ru_RU')

class Generator_fake:
	def start_gen(self):
		fake_results = "  ┌─[+] Фейк Личность (Имя):\n"
		fake_results += f"├ Полное имя: {fake.name()}\n"
		fake_results += f"├ Имя: {fake.first_name()}\n"
		fake_results += f"├ Фамилия: {fake.last_name()}\n"
		fake_results += f"├ Префикс: {fake.prefix()}\n"
		fake_results += f"└ Суффикс: {fake.suffix()}\n"
		fake_results += " ┌─[+] Адреса:\n"
		fake_results += f"├ Адрес: {fake.address()}\n"
		fake_results += f"├ Адрес улицы: {fake.street_address()}\n"
		fake_results += f"├ Страна: {fake.country()}\n"
		fake_results += f"└ Город: {fake.city()}\n" 
		fake_results += " ┌─[+] Телефон и интернет:\n"
		fake_results += f"├ Номер телефона: {fake.phone_number()}\n"
		fake_results += f"├ Почта: {fake.email()}\n"
		fake_results += f"├ URL: {fake.url()}\n"
		fake_results += f"├ Доменное имя: {fake.domain_name()}\n"
		fake_results += f"├ IPv4: {fake.ipv4()}\n"
		fake_results += f"└ IPv6: {fake.ipv6()}\n"
		fake_results += " ┌─[+] Дата:\n"
		fake_results += f"├ Дата: {fake.date()}\n"
		fake_results += f"├ Дата рождения: {fake.date_of_birth()}\n"
		fake_results += f"├ Дата и время: {fake.date_time()}\n"
		fake_results += f"├ Год: {fake.year()}\n"
		fake_results += f"├ Месяц: {fake.month()}\n"
		fake_results += f"└ Неделя: {fake.day_of_week()}\n"
		fake_results += " ┌─[+] Текстовые данные:\n"
		fake_results += f"├ Текст: {fake.text()}\n"
		fake_results += f"├ Предложение: {fake.sentence()}\n"
		fake_results += f"├ Абзац: {fake.paragraph()}\n"
		fake_results += f"└ Слово: {fake.word()}\n"
		fake_results += " ┌─[+] Финансовые данные:\n"
		fake_results += f"├ Номер кредитной карты: {fake.credit_card_number()}\n"
		fake_results += f"├ Провайдер кредитной карты: {fake.credit_card_provider()}\n"
		fake_results += f"├ Срок действия кредитной карты: {fake.credit_card_expire()}\n"
		fake_results += f"└ Валюта: {fake.currency()}\n"
		fake_results += " ┌─[+] Прочее:\n"
		fake_results += f"├ UUID: {fake.uuid4()}\n"
		fake_results += f"├ Компания: {fake.company()}\n"
		fake_results += f"├ Должность: {fake.job()}\n"
		fake_results += f"├ Язык: {fake.language_name()}\n"
		fake_results += f"└ Цвет: {fake.color_name()}\n"
		fake_results += " ┌─[+] Географические данные:\n"
		fake_results += f"├ Широта: {fake.latitude()}\n"
		fake_results += f"└ Долгота: {fake.longitude()}\n"
		fake_results += " ┌─[+] Локализация:\n"
		fake_results += f"└ Язык: {fake.locales[0]}\n"
		fake_results += " ┌─[+] Дополнительно:\n"
		fake_results += f"└ Логин: {fake.user_name()}\n"

		print(f"{pink}{fake_results}{reset}")