import telebot
from telebot import types

TOKEN = '8840792965:AAFrckbsQuuAGT8A3JzwgJexG3KqYM7E30'  # BotFather'dan olingan tokeningiz
WEB_APP_URL = 'https://telegram-bot-mini-app-orcin.vercel.app'

bot = telebot.TeleBot(TOKEN)

# Har bir til uchun matnlar
texts = {
    'uz': {
        'choose': "Tilni tanlang:",
        'welcome': "Xush kelibsiz! Treyding jamiyatimizga xush kelibsiz.",
        'btn': "🚀 Mini Ilovani Ochish"
    },
    'ru': {
        'choose': "Выберите язык:",
        'welcome': "Добро пожаловать! Добро пожаловать в наше трейдинг сообщество.",
        'btn': "🚀 Открыть Mini App"
    },
    'en': {
        'choose': "Choose language:",
        'welcome': "Welcome! Welcome to our trading community.",
        'btn': "🚀 Open Mini App"
    }
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    btn_uz = types.InlineKeyboardButton("🇺🇿 O'zbek", callback_data='lang_uz')
    btn_ru = types.InlineKeyboardButton("🇷🇺 Русский", callback_data='lang_ru')
    btn_en = types.InlineKeyboardButton("🇬🇧 English", callback_data='lang_en')
    markup.add(btn_uz, btn_ru, btn_en)
    
    bot.send_message(message.chat.id, "Tilni tanlang / Выберите язык / Choose language:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('lang_'))
def handle_language(call):
    lang = call.data.split('_')[1]
    t = texts.get(lang, texts['uz'])
    
    markup = types.InlineKeyboardMarkup()
    web_app = types.WebAppInfo(url=WEB_APP_URL)
    btn_app = types.InlineKeyboardButton(t['btn'], web_app=web_app)
    markup.add(btn_app)
    
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=t['welcome'],
        reply_markup=markup
    )

bot.infinity_polling()
