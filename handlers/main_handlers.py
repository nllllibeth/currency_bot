import logging
import time

from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from loader import bot
from keyboards.currencies_kb import inline_currencies
from binance_api.exchange_info import get_price, get_avg_price, get_historical_data, plotting, removing_picture, price_change_percent


async def get_start(message : Message, state: FSMContext):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    async with state.proxy() as data:
        data['user_id'] = user_id
    logging.info(f"{user_id} {user_first_name} {time.asctime()}")
    await message.reply(f"Hi, {user_first_name}!\n\nPlease select cryptocurrency that you want to get info about", reply_markup=inline_currencies)


async def button_pressed(call : CallbackQuery, state: FSMContext):
    currency_name = call.data.split('_')[1]
    symbol = currency_name + "USDT"
    price = get_price(symbol)
    avg_price = get_avg_price(symbol)
    data = get_historical_data(symbol, '12h', '1w')
    chart_name = plotting(data, symbol)
    price_change24h = price_change_percent(symbol)
    async with state.proxy() as data:
        await bot.send_photo(data['user_id'], 
                             photo=open(chart_name, 'rb'),
                             caption=f"{currency_name} Price Chart for last week\n\nINFO about {currency_name}\n\nCurrent price   ---   {price}   USDT \nAverage price   ---   {avg_price}   USDT\nPrice change percent for last 24h   ---   {price_change24h}   %")
    await call.answer()
    removing_picture(chart_name)



    


