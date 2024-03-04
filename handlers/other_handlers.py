from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command

from lexicon.lexicon_ru import LEXICON_RU

router = Router()

@router.message(Command(commands='delmenu'))
async def del_menu(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer(text='Кнопка "Menu" удалена')

@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])
