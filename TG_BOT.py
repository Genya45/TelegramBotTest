import telebot
from telebot import types
bot = telebot.TeleBot('2140825407:AAH4D5GyRhgfMxHyHrsJt3kmBv925ICVaTc')


def botSend(call):
    bot.send_message(call.message.chat.id, 'Неужели, ' + str(call.from_user.first_name) + ', да ваше идеальное место работы - '+ str(result[sex][profit]))
    bot.send_message(call.message.chat.id, 'Начать заново /start')




sex = 0
profit = 0
mode = 0

result = [["Завод","Програмист ","Сварщик"],["Домохозяйка ","Дизайнер ","Ноготочки"],["Грузовой вертолет","Многоцелевой вертолет","Ударный вертолёт McDonnell Douglas AH-64 Apache"]]



def get_sex(message):
    global mode
    mode = 1
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='М', callback_data='М'))
    keyboard.add(types.InlineKeyboardButton(text='Ж', callback_data='Ж'))
    keyboard.add(types.InlineKeyboardButton(text='Атакующий вертолет', callback_data='В'))
    bot.send_message(message.from_user.id, text="Какой твой пол?", reply_markup=keyboard)

def get_profit(call):    
    global mode
    mode = 2
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='< $10к', callback_data='< $10к'))
    keyboard.add(types.InlineKeyboardButton(text='> $10к', callback_data='> $10к'))
    keyboard.add(types.InlineKeyboardButton(text='$100500', callback_data='$100500'))
    bot.send_message(call.message.chat.id, text="Ожидаемый доход", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global mode
    global sex
    global profit
    if call.data == "М":
        sex = 0
    elif call.data == "Ж":
        sex = 1
    elif call.data == "В":
        sex = 2
    elif call.data == "< $10к":
        profit = 0
    elif call.data == "> $10к":
        profit = 1
    elif call.data == "$100500":
        profit = 2




    
    if mode == 1:
        get_profit(call)
    elif mode == 2:
        botSend(call)


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Начало опроса')
        get_sex(message)
    else:
        mode = 0
        bot.send_message(message.from_user.id, 'Начать опрос /start')


bot.polling(none_stop=True, interval=0)
