import csv
from core.colors import pink, reset

class TelegramOSINT:
    def __init__(self, telegram_id):
        self.telegram_id = str(telegram_id)  # в строку для удобства сравнения

    def telegram_checker(self):
        files = [f'telegram_base/EYEOFGOD_{i}.csv' for i in range(33)]  # EYEOFGOD_0.csv до EYEOFGOD_32.csv
        files[0] = 'telegram_base/EYEOFGOD.csv'  # если нулевой файл называется иначе

        for file in files:
            try:
                with open(file, mode='r', encoding='utf-8') as f:
                    reader = csv.reader(f, delimiter=',')
                    next(reader)  # пропускаем заголовок

                    for row in reader:
                        if row[0] == self.telegram_id:
                            user_id = row[0]
                            username = row[1]
                            phone = row[2]
                            first_name = row[3]
                            last_name = row[4]

                            results = f"""
ID: {user_id}
username: {username}
номер: {phone}
имя: {first_name}
фамилия: {last_name}
"""
                            print(f"{pink}{results}{reset}")
                            return  # нашли, заканчиваем

            except FileNotFoundError:
                # Если файл отсутствует, можно пропустить или вывести предупреждение
                continue

        print("Пользователь не найден в базах.")
