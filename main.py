# -Простой скрипт для автоматического участия в розыгрышах telegram premium
from telethon.errors.rpcerrorlist import PhoneNumberBannedError, PasswordHashInvalidError, UsernameInvalidError
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon.sync import TelegramClient, events
import datetime
import asyncio
import json
import os

from config import MIN_MONTHS_PREMIUM, DEVICE_MODEL, SYSTEM_VERSION, CHANNELS, COUNTRY, AUTO_LEAVE_CHANNELS

logo = """
▄▀█ █░█ ▀█▀ █▀█ █▀█ ▄▀█ █▀█ ▀█▀ █ █▀▀|ᵇʸ ᵈᵉˡᵃᶠᵃᵘˡᵗ
█▀█ █▄█ ░█░ █▄█ █▀▀ █▀█ █▀▄ ░█░ █ █▄▄
"""

# -Определение принтов
def gd_print(value):
    green_color = '\033[32m'
    reset_color = '\033[0m'
    result = f"\n>{green_color} {value} {reset_color}\n"
    print(result)

def bd_print(value):
    red_color = '\033[31m'
    reset_color = '\033[0m'
    result = f"\n>{red_color} {value} {reset_color}\n"
    print(result)

# -Получение данных об аккаунтах (пока что можно использовать только один аккаунт, так как за один раз большее количество ведёт к бану аккаунтов)
with open('accounts.json', 'r') as file:
    data = json.load(file)
    phone_number = data['accounts'][0]['phone']

# -Определяем client, передаём необходимые данные
client = TelegramClient(
    session = f"tg_{phone_number}",
    api_id = data['accounts'][0]['api_id'],
    api_hash = data['accounts'][0]['api_hash'],
    device_model = DEVICE_MODEL,
    system_version = SYSTEM_VERSION
)

# -Функция для ожидания завершения розыгрыша
async def job_wait(date, channels):
    delta = date - datetime.datetime.now()
    await asyncio.sleep(delta.total_seconds())
    await asyncio.sleep(3600)
    try:
        for channel in channels:
            await client(LeaveChannelRequest(channel))
            print(f"Розыгрыш в канале {channel} был завершён. Вышел из него.")
    except Exception as e:
        bd_print(f"Неизвестная ошибка: {e}")

# -Функция для получения и обработки сообщений о розыгрышах
@client.on(events.NewMessage(CHANNELS))
async def general_handler(event):
    try:
        if event.message.media.months >= MIN_MONTHS_PREMIUM:
            if event.message.media.countries_iso2 is None or COUNTRY in event.message.media.countries_iso2:
                date = str(event.message.media.until_date)[:-9]
                date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M")

                gd_print(f"Получили информацию о розыгрыше на {event.message.media.months} месяца.")
                channels = event.message.media.channels
                for channel in channels:
                    await client(JoinChannelRequest(channel))
                    print(f"Вступили в канал {channel}")

                if AUTO_LEAVE_CHANNELS:
                    await job_wait(date, channels)

    except AttributeError:
        pass
    except TypeError:
        pass
    except Exception as e:
        bd_print(f"Неизвестная ошибка: {e}")

# -Запуск, чистка консоли и вывод лого
if __name__ == "__main__":
    try:
        client.start(phone=phone_number)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        gd_print(f"Успешно вошли в аккаунт {phone_number}.")

        client.run_until_disconnected()
    except PhoneNumberBannedError:
        bd_print(f"Аккаунт {phone_number} заблокирован.")
    except PasswordHashInvalidError:
        bd_print(f"Неверный пароль для аккаунта {phone_number}.")
    except UsernameInvalidError:
        pass
    except Exception as e:
        bd_print(f"Неизвестная ошибка: {e}")
