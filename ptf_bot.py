#!/usr/bin/env python3
"""
ПТФ Каталог — Telegram Bot
Запуск: python3 ptf_bot.py
Требует: pip install pyTelegramBotAPI
"""

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# ⚠️ ЗАМЕНИТЕ ТОКЕН на новый после отзыва старого через @BotFather → /revoke
TOKEN = "8734903858:AAHcVhJ089UKx1HRLic1huqx5IKiygX-RqQ"

CATALOG_URL = "https://lively-tiramisu-c6f315.netlify.app/"

bot = telebot.TeleBot(TOKEN)

# ===== /start =====
@bot.message_handler(commands=['start'])
def start(message):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(
        text="📦 Открыть каталог ПТФ",
        web_app=WebAppInfo(url=CATALOG_URL)
    ))
    kb.add(InlineKeyboardButton(
        text="🔗 Открыть в браузере",
        url=CATALOG_URL
    ))
    bot.send_message(
        message.chat.id,
        "👋 *Привет!*\n\n"
        "Это каталог противотуманных фар ПТФ.\n\n"
        "📦 *93 артикула* — WD и GQ серии\n"
        "🚗 Подбор по марке и модели автомобиля\n"
        "🔍 Быстрый поиск по артикулу\n\n"
        "Нажмите кнопку чтобы открыть каталог:",
        parse_mode='Markdown',
        reply_markup=kb
    )

# ===== /catalog =====
@bot.message_handler(commands=['catalog'])
def catalog(message):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(
        text="📦 Открыть каталог",
        web_app=WebAppInfo(url=CATALOG_URL)
    ))
    bot.send_message(message.chat.id, "Открываю каталог ПТФ 👇", reply_markup=kb)

# ===== /help =====
@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.send_message(
        message.chat.id,
        "📋 *Команды бота:*\n\n"
        "/start — Приветствие и кнопка каталога\n"
        "/catalog — Открыть каталог ПТФ\n"
        "/help — Помощь\n\n"
        f"🔗 Прямая ссылка: {CATALOG_URL}",
        parse_mode='Markdown'
    )

# ===== Любое сообщение =====
@bot.message_handler(func=lambda m: True)
def any_message(message):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(
        text="📦 Открыть каталог ПТФ",
        web_app=WebAppInfo(url=CATALOG_URL)
    ))
    bot.send_message(
        message.chat.id,
        "Нажмите кнопку для открытия каталога 👇",
        reply_markup=kb
    )

print("✅ Бот запущен. Нажмите Ctrl+C для остановки.")
bot.infinity_polling()
