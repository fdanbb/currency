from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import cbrfService
import koronaService

bot = Bot(token='5467419228:AAFnIowJUyw4VVK7OPn9_uxb4JQn0yMVIPk')
dp = Dispatcher(bot)

buttonUsd = KeyboardButton('Курс доллара')
buttonEuro = KeyboardButton('Курс евро')
buttonLira = KeyboardButton('Курс лиры')
keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonUsd).add(buttonEuro).add(
    buttonLira)


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.answer("Курс какой валюты вы хотите узнать?", reply_markup=keyboard)


@dp.message_handler()
async def usd(message: types.Message):
    if message.text == 'Курс доллара':
        await message.answer(
            "ЦБ РФ: " + str(cbrfService.getUsdPrice()) + "\nКорона: " + str(koronaService.getUsdPrice()), reply_markup=keyboard)
    elif message.text == 'Курс евро':
        await message.answer(
            "ЦБ РФ: " + str(cbrfService.getEuroPrice()) + "\nКорона: " + str(koronaService.getEuroPrice()), reply_markup=keyboard)
    elif message.text == 'Курс лиры':
        await message.answer(
            "ЦБ РФ: " + str(cbrfService.getLiraPrice()) + "\nКорона: " + str(koronaService.getLiraPrice()), reply_markup=keyboard)


executor.start_polling(dp)
