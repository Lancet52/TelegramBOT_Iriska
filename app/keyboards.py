from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from aiogram import Router


router_key = Router()


main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Игры', callback_data='games')],
                                             [InlineKeyboardButton(text='Рассказать анекдот', callback_data='joke')],
                                             [InlineKeyboardButton(text='Занимательные тесты', url='https://www.karusel-tv.ru/news/test')]])


inline_games = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='🎲 Бросить кубик', callback_data='dice')],
                                                   [InlineKeyboardButton(text='🎯 Дартс', callback_data='darts')],
                                                   [InlineKeyboardButton(text='🏀 Баскетбол', callback_data='basketball')],
                                                   [InlineKeyboardButton(text='⚽ Футбол', callback_data='football')],
                                                   [InlineKeyboardButton(text='🎳 Боулинг', callback_data='bowling')],
                                                   [InlineKeyboardButton(text='🎰 Казино', callback_data='casino')],
                                                   [InlineKeyboardButton(text='🔴 На главную 🔴', callback_data='main')]])

inline_joke=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Ещё шутейку!',callback_data='joke')],
                                                  [InlineKeyboardButton(text='🔴 На главную 🔴', callback_data='main')]])

