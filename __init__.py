
import telebot



bot = telebot.TeleBot("1086800436:AAHiX4Tw9F4wRT7SaevYrszA1l5zFslYjyY")
@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.reply_to(message, "Грация блять!")
    
    
bot.polling(none_stop=True)