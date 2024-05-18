import random

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb
from app.joke import joke_dict

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет! Я Ириска. И я твой друг бот!', reply_markup=kb.main)


@router.message(Command('кубик', prefix="/!%"))
async def cmd_dice(message: Message):
    await message.answer_dice(emoji="🎲")


@router.message(Command('дартс', prefix="/!%"))
async def cmd_darts(message: Message):
    await message.answer_dice(emoji="🎯")


@router.message(Command('баскетбол', prefix="/!%"))
async def cmd_basketball(message: Message):
    await message.answer_dice(emoji="🏀")


@router.message(Command('футбол', prefix="/!%"))
async def cmd_football(message: Message):
    await message.answer_dice(emoji="⚽")


@router.message(Command('боулинг', prefix="/!%"))
async def cmd_bowling(message: Message):
    await message.answer_dice(emoji="🎳")


@router.message(Command('казино', prefix="/!%"))
async def cmd_cazino(message: Message):
    await message.answer_dice(emoji="🎰")


@router.message(F.text)
async def info(message: Message):
    keywords_hi = ('привет', 'здравствуй')
    for k in keywords_hi:
        if k in message.text.lower():
            priv = ('Дарова, ', 'Привет, ', 'Здравствуй, ', 'Прив, ', 'Здарова, ')
            await message.reply(str(random.choice(priv)) + f'{message.from_user.first_name} 🙋‍♂')
            break


@router.callback_query(F.data == 'main')
async def games(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Привет! Я Ириска. И я твой друг бот!', reply_markup=kb.main)


# Коллбэки на миниигры:
@router.callback_query(F.data == 'games')
async def games(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Выбери миниигру!', reply_markup=kb.inline_games)


@router.callback_query(F.data == 'dice')
async def dice(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_dice(emoji="🎲")
    await callback.message.delete()


@router.callback_query(F.data == 'darts')
async def dice(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_dice(emoji="🎯")
    await callback.message.delete()


@router.callback_query(F.data == 'basketball')
async def dice(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_dice(emoji="🏀")
    await callback.message.delete()


@router.callback_query(F.data == 'football')
async def dice(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_dice(emoji="⚽")
    await callback.message.delete()


@router.callback_query(F.data == 'bowling')
async def dice(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_dice(emoji="🎳")
    await callback.message.delete()


@router.callback_query(F.data == 'casino')
async def dice(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_dice(emoji="🎰")
    await callback.message.delete()


@router.callback_query(F.data == 'joke')
async def joke1(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(random.choice(joke_dict),reply_markup=kb.inline_joke)

