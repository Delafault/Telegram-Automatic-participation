MIN_MONTHS_PREMIUM = 3 # -Можно указать, от скольки месяцев розыгрыша telegram premium бот будет участвовать. Если во всех, то укажите '3' или меньше.
CHANNELS = None # -Каналы для отслеживания розыгрышей (например, razdacha_TelegramPremium или tgpremiumdrops без символа '@', перечислять в кавычках через запятую: "razdacha_TelegramPremium", "tgpremiumdrops"). Значение 'None' означает, что бот будет получать сообщения о розыгрышах в любом канале (при этом значении вы также можете отправлять ему сообщение о розыгрыше сами)
AUTO_LEAVE_CHANNELS = True # -Если True, то бот выходит из каналов после завершения розыгрыша (бывает полезно, так как телеграм не даёт вступать в большое количество каналов). В противном случае ставьте False.
COUNTRY = 'RU' # -Страна, номер которой используется в вашем аккаунте (например, '+7' - это 'RU'). Рекомендуется заполнить, чтобы не участвовать в розыгрышах, в которых вы не можете участвовать из-за ограничений стран в розыгрыше.

# -Не обязательно для заполнения или изменения
DEVICE_MODEL = "Pixel 3 XL"
SYSTEM_VERSION = "Android 10.0"