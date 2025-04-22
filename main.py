import telebot
from telegram_bot.handlers import setup_handlers
from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

def main():
    bot = telebot.TeleBot(API_TOKEN)
    setup_handlers(bot)
    print("Bot is running...")
    bot.infinity_polling()

if __name__ == '__main__':
    main()