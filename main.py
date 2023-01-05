from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
import requests


# MANBA : @MistrUZ | @MrGayratov
# API MANBA : @ITMAKTABI1 | @SuppercoderUz
# MANBAGA TEGILMASIN !!!

TOKEN = "5880875816:AAEHvVbLV4rmMK5tyMgEeMtu7bKwCCp7C9E"
bot = Bot(token=TOKEN, parse_mode='markdown')
Gayratov = Dispatcher(bot)

channel = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Bizning Kanal",url="https://t.me/+JT-0vrUbPhkxNTQ6")]])

@Gayratov.message_handler(commands=['start'])
async def HGADM(message: types.Message):
    await message.reply(f"*👋Assalamu aleykum {message.from_user.first_name}\n🤖: Men krill-lotin va lotin-krill ga bexato o'girb beraman!*",reply_markup=channel)

@Gayratov.message_handler()
async def HGADM(message: types.Message):
    api = requests.get(f"http://supercoders.uz/lotin.php?text={message.text}").json()
    api= (api[0])
    await message.reply(f"{api}")

if __name__ == '__main__':
    executor.start_polling(Gayratov)