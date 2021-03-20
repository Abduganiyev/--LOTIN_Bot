from transliterate import to_cyrillic,to_latin
import telebot
bot = telebot.TeleBot("1517496555:AAFEyYOTfJyjNWBrQUIkDGZiwoDxrbAZeCk")
@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg="Assalomu aleykom, Xush kelibsiz!"
    msg+="\nMatn kiriting:"
    bot.reply_to(message,msg)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg=message.text
    javob=lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message,javob(msg))
bot.polling()