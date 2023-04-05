import os

import telebot
import webbrowser
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.environ["TELEGRAM_TOKEN"])


@bot.message_handler(commands=["site", "website"])
def site(message):
    webbrowser.open("https://github.com/Paul-Starodub/my_bot")


@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(message.chat.id, f"Hello, {message.from_user.first_name}")


@bot.message_handler(commands=["help"])
def main(message):
    bot.send_message(
        message.chat.id, "<b>Help</> <em>information</em>", parse_mode="html"
    )


@bot.message_handler()
def info(message):
    if message.text.lower() == "hello":
        bot.send_message(message.chat.id, "How are you?")
    elif message.text.lower() == "id":
        bot.reply_to(message, f"ID: {message.from_user.id}")


bot.polling(none_stop=True)
