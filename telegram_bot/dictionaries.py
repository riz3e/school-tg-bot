english_dict = {
    "hi": "Hello there! 👋",
    "hello": "Hi! How can I help you today?",
    "how are you": "I'm just a bot, but I'm functioning well! 🤖",
    "bye": "Goodbye! Have a nice day! 🌞",
    "thanks": "You're welcome! 😊",
    "what can you do": "I can translate phrases, tell jokes, show weather info and more! Try /help",
    "joke": "Why don't scientists trust atoms? Because they make up everything! 😄",
    "weather": "Currently I can't check real weather, but you can ask Google! ☀️⛈️",
    "time": "I don't have a clock, but you can check time with /time command! ⏰",
    "help": "I can help with translations, jokes and basic info. Try commands: /start, /help, /time, /joke, /weather"
}

kazakh_dict = {
    "сәлем": "Сәлеметсіз бе! 👋",
    "салем": "Сәлем! Қазір қалай көмектесе аламын?",
    "қалыңыз қалай": "Мен ботпын, бірақ жақсы жұмыс істеп тұрмын! 🤖",
    "сау болыңыз": "Сау болыңыз! Күніңіз жақсы өтсін! 🌞",
    "рахмет": "Рақмет сізге! 😊",
    "сен не істей аласың": "Мен аударма жасай аламын, анекдот айта аламын, ауа райы туралы айта аламын және т.б! /help командасын қолданыңыз",
    "анекдот": "Әрбір шеккен темекі өмірімізді екі сағатқа қысқартады, әрбір ішкен арақ өмірімізді үш сағатқа қысқартады, ал әрбір жұмыс күні өмірімізді сегіз сағатқа қысқартады.",
    "ауа райы": "Қазіргі уақытта мен нақты ауа райын тексере алмаймын, бірақ Google-дан сұрай аласыз! ☀️⛈️",
    "уақыт": "Менде сағат жоқ, бірақ сіз /time командасын қолдана аласыз! ⏰",
    "көмек": "Мен аудармамен, анекдоттармен және негізгі ақпаратпен көмектесе аламын. Командаларды қолданып көріңіз: /start, /help, /time, /joke, /weather"
}

russian_dict = {
    "привет": "Здравствуйте! 👋",
    "здравствуй": "Привет! Чем могу помочь?",
    "как дела": "Я всего лишь бот, но у меня всё хорошо! 🤖",
    "пока": "До свидания! Хорошего дня! 🌞",
    "спасибо": "Пожалуйста! 😊",
    "что ты умеешь": "Я могу переводить фразы, рассказывать анекдоты, показывать погоду и многое другое! Попробуйте /help",
    "анекдот": "Почему доктор не стал лечить больного раком? Неудобно просто)",
    "погода": "Сейчас я не могу проверить реальную погоду, но вы можете спросить у Google! ☀️⛈️",
    "время": "У меня нет часов, но вы можете проверить время командой /time! ⏰",
    "помощь": "Я могу помочь с переводом, анекдотами и основной информацией. Попробуйте команды: /start, /help, /time, /joke, /weather"
}

def get_response(text, language):
    text = text.lower()
    if language == 'English':
        return english_dict.get(text, "I don't understand that yet. Try /help for commands list.")
    elif language == 'Kazakh':
        return kazakh_dict.get(text, "Мен бұны әлі түсінбеймін. Командалар тізімі үшін /help қолданыңыз.")
    elif language == 'Russian':
        return russian_dict.get(text, "Я пока это не понимаю. Попробуйте /help для списка команд.")
    return "Please select a language first with /start command"