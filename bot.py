import telebot

# Создаем экземпляр бота
bot = telebot.TeleBot('7184165168:AAHVDg6MoCyUzgvWEDCx0PidNFBCCifkOV4')

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, f'Здраствуйте, {message.from_user.first_name}  {message.from_user.last_name}')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Бот запущен. Начните общение с ним.')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
    if message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

# Запускаем бота
bot.polling(none_stop=True, interval=0)





