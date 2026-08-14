user_name = input("Добрый день, я - Бот помощник по спорту, как я могу к тебе обращаться?\n")
user_age = int(input(f"Привет, {user_name}! Сколько тебе лет?\n"))
user_weight = float(input(f"Отлично, {user_name}! Сколько ты весишь (в кг)?\n").replace(',', '.')) # .replace нагуглил для защиты от неккоректного вода
user_height = float(input(f"Принял, {user_name}! А теперь скажи какой у тебя рост (в метрах)?\n").replace(',', '.')) # .replace нагуглил для защиты от неккоректного вода
# расчёт индекса массы тела
bmi_value_round = round(user_weight / (user_height ** 2), 1)
# расчёт потребления воды в течение дня
water_l = user_weight * 30 / 1000

print(f"Отчет для пользователя: {user_name} ({user_age})\nТвой Индекс Массы Тела: {bmi_value_round}\nРекомендуемая норма воды: {water_l:.1f} л. в день\n\nРасчет окончен. Будьте здоровы! ")