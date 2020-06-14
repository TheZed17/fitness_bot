import telebot
from telebot import types

bot = telebot.TeleBot('1236406662:AAECVfMXQ2KKblDllvDlC4xqAOWCOrmf5us')


@bot.message_handler(commands=['start'])
def start(message):
    sticker = open('static/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Понедельник')
    btn2 = types.KeyboardButton('Среда')
    btn3 = types.KeyboardButton('Пятница')
    btn4 = types.KeyboardButton('Кардио тренировка')
    markup.add(btn1, btn2, btn3, btn4)
    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!\nКакой день вас " \
                f"интересует? "
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "начать тест заново":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Понедельник')
        btn2 = types.KeyboardButton('Среда')
        btn3 = types.KeyboardButton('Пятница')
        btn4 = types.KeyboardButton('Кардио тренировка')
        markup.add(btn1, btn2, btn3, btn4)
        final_message = "Решил попробовать что-то ещё? \nКакие мышцы вас интересуют?:"

    elif get_message_bot == "понедельник":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Упражнения на ноги в домашних условиях", url="https://www.youtube.com/watch?v=1pWtVHUo9ic"))
        markup.add(types.InlineKeyboardButton("Упражнения на пресс в домашних условиях", url="https://www.youtube.com/watch?v=j0MYBjLK6Pc"))
        final_message = "1.Приседания плие с гантелей\n2.Выпады назад с гантелями\n3.Мертвая тяга\n4.Подъем на носки стоя\n5.Скручивание на пресс\n✅ Количество рабочих подходов в упражнении : 3-4\n✅ Количество повторений: 10 - 15\n✅ Отдых между подходами: 2 - 3 минуты\n✅ Рабочий вес подбирается в зависимости от ваших физических данных"

    elif get_message_bot == "среда":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Упражнения на грудные мыщцы в домашних условиях", url="https://www.youtube.com/watch?v=VTkLF_aMjk0"))
        markup.add(types.InlineKeyboardButton("Упражнения на плечи в домашних условиях", url="https://www.youtube.com/watch?v=FKIRaeF7r4E"))
        final_message = "1.Жим гантель лежа\n2.Разведение гантель лежа\n3.Пуловер\n4.Жим гантель сидя\n5.Махи с гантелями стоя\n✅ Количество рабочих подходов в упражнении : 3-4\n✅ Количество повторений: 10 - 15\n✅ Отдых между подходами: 2 - 3 минуты\n✅ Рабочий вес подбирается в зависимости от ваших физических данных"

    elif get_message_bot == "пятница":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Упражнения на спину в домашних условиях", url="https://www.youtube.com/watch?v=wT8jFMDJ390"))
        markup.add(types.InlineKeyboardButton("Упражнения на руки в домашних условиях", url="https://www.youtube.com/watch?v=Q5_r1cekWOc&t=2s"))
        final_message = "1.Тяга гантель в наклоне\n2.Тяга гантели к бедру\n3.Подъем гантель на бицепс стоя\n4.Молотки с гантелями\n5.Французский жим сидя\n✅ Количество рабочих подходов в упражнении : 3-4\n✅ Количество повторений: 10 - 15\n✅ Отдых между подходами: 2 - 3 минуты\n✅ Рабочий вес подбирается в зависимости от ваших физических данных"

    elif get_message_bot == 'кардио тренировка':
        markup = types.InlineKeyboardMarkup()
        final_message = "<a href='https://www.youtube.com/watch?v=oKuOIW81eX0'>💪Тренировка для сжигания жира в домашних условиях</a>"

    # Здесь различные дополнительные проверки и условия
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Понедельник')
        btn2 = types.KeyboardButton('Среда')
        btn3 = types.KeyboardButton('Пятница')
        btn4 = types.KeyboardButton('Кардио тренировка')
        markup.add(btn1, btn2, btn3, btn4)
        final_message = "Так, так, так\nПостой, лучше нажми на одну из интерактивных кнопок ниже"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)