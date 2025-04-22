from telebot import types
from telegram_bot.keyboards import language_keyboard, remove_keyboard, main_menu_keyboard
from telegram_bot.dictionaries import get_response
import datetime

# Store user language preferences
user_languages = {}

def setup_handlers(bot):
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        user_name = message.from_user.first_name
        bot.reply_to(message, f"Hello, {user_name}! I'm your personal assistant bot.", 
                    reply_markup=remove_keyboard())
        bot.send_message(message.chat.id, "Please choose your language:", 
                        reply_markup=language_keyboard())

    @bot.message_handler(commands=['help'])
    def send_help(message):
        user_lang = user_languages.get(message.chat.id, 'English')
        response = get_response("help", user_lang)
        bot.reply_to(message, response, reply_markup=main_menu_keyboard(user_lang))

    @bot.message_handler(commands=['time'])
    def send_time(message):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        bot.reply_to(message, f"Current time is: {current_time}")

    @bot.message_handler(commands=['joke'])
    def send_joke(message):
        user_lang = user_languages.get(message.chat.id, 'English')
        response = get_response("joke", user_lang)
        bot.reply_to(message, response)

    @bot.message_handler(commands=['weather'])
    def send_weather(message):
        user_lang = user_languages.get(message.chat.id, 'English')
        response = get_response("weather", user_lang)
        bot.reply_to(message, response)

    @bot.message_handler(func=lambda message: message.text in ['English', 'Kazakh', 'Russian'])
    def handle_language_selection(message):
        user_languages[message.chat.id] = message.text
        greeting = {
            'English': "Great choice! What would you like to do?",
            'Kazakh': "Тамаша таңдау! Сізге не қызықтырады?",
            'Russian': "Отличный выбор! Чем бы вы хотели заняться?"
        }[message.text]
        bot.send_message(message.chat.id, greeting, 
                        reply_markup=main_menu_keyboard(message.text))

    @bot.message_handler(func=lambda message: True)
    def handle_all_messages(message):
        user_lang = user_languages.get(message.chat.id, None)
        if not user_lang:
            bot.reply_to(message, "Please select a language first with /start command")
            return
        response = get_response(message.text, user_lang)
        bot.reply_to(message, response)