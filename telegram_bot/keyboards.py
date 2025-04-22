from telebot import types

def language_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    btn_eng = types.KeyboardButton('English')
    btn_kaz = types.KeyboardButton('Kazakh')
    btn_rus = types.KeyboardButton('Russian')
    markup.add(btn_eng, btn_kaz, btn_rus)
    return markup

def main_menu_keyboard(language='English'):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    
    if language == 'English':
        btn_help = types.KeyboardButton('Help')
        btn_joke = types.KeyboardButton('Joke')
        btn_time = types.KeyboardButton('Time')
        btn_weather = types.KeyboardButton('Weather')
    elif language == 'Kazakh':
        btn_help = types.KeyboardButton('Көмек')
        btn_joke = types.KeyboardButton('Анекдот')
        btn_time = types.KeyboardButton('Уақыт')
        btn_weather = types.KeyboardButton('Ауа райы')
    else:  # Russian
        btn_help = types.KeyboardButton('Помощь')
        btn_joke = types.KeyboardButton('Анекдот')
        btn_time = types.KeyboardButton('Время')
        btn_weather = types.KeyboardButton('Погода')
    
    markup.add(btn_help, btn_joke, btn_time, btn_weather)
    return markup

def remove_keyboard():
    return types.ReplyKeyboardRemove()