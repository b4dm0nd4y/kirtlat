# Импорт библиотек
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message  #ловим все обновления этого типа
from aiogram.filters.command import Command #обрабатываем команды /start, /help, etc

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

translit_d = {
        "а": 'a',
        "б": 'b',
        "в": 'v',
        "г": 'g',
        "д": 'd',
        "е": 'e',
        "ё": 'e',
        "ж": 'zh',
        "з": 'z',
        "и": 'i',
        "й": 'i',
        "к": 'k',
        "л": 'l',
        "м": 'm',
        "н": 'n',
        "о": 'o',
        "п": 'p',
        "р": 'r',
        "с": 's',
        "т": 't',
        "у": 'u',
        "ф": 'f',
        "х": 'kh',
        "ц": 'ts',
        "ч": 'ch',
        "ш": 'sh',
        "щ": 'shch',
        "ы": 'y',
        "ъ": 'ie',
        "э": 'e',
        "ю": 'iu',
        "я": 'ia',
        " ": " "
}

kirilic=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя ')

def validate_msg(msg):
    for ch in msg.lower():
        if ch not in kirilic: 
            return False

    return True

    


@dp.message(Command(commands=['start']))
async def proccess_command_start(msg):
    username = msg.from_user.full_name
    user_id = msg.from_user.id
    text = f'Приветствую тебя, {username}! Напиши своё ФИО кириллицей и я переведу его на латиницу.'

    logging.info(f'{username} {user_id} запустил бота')
 
    await bot.send_message(chat_id=user_id, text=text)
 
   
@dp.message()
async def translate_msg(msg): 
    username = msg.from_user.full_name
    user_id = msg.from_user.id
    text = msg.text
    logging.info(f'{username} {user_id}: отправил {text}') 

    if validate_msg(text):
        text = "".join(translit_d[ch] for ch in text.lower()).title()
    else:
        text = "Пожалуйста напишите ваше ФИО, используя только кириллицу и пробелы."

    await msg.answer(text=text)





if __name__ == '__main__':
    dp.run_polling(bot)
