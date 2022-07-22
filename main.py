import telebot

api_token = 'token'

venum_bot = telebot.TeleBot(api_token)

keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard.row('Яндекс', 'Доставка')

@venum_bot.message_handler(commands=['start'])
def start_message(message):
    venum_bot.send_message(message.chat.id, 'Отправь мне любое сообщение или стикер', reply_markup=keyboard)

@venum_bot.message_handler(content_types=['text'])
def echo(message):
    venum_bot.send_message(message.chat.id, text=f"{message.text}")

@venum_bot.message_handler(content_types=["sticker"])
def handle_docs_audio(message):
    sticker_id = message.sticker.file_id
    venum_bot.send_sticker(message.chat.id, sticker_id)

venum_bot.polling(none_stop=True)