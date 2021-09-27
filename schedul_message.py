import logging
import asyncio
import datetime
import aioschedule
from loader import dp, bot
from aiogram.types import CallbackQuery
from database import select_user_dinner_tomorrow, the_users_without_dinner
from keyboards.default.menu import menu_garnish, inline_yes_no


@dp.message_handler()
async def choose_your_dinner():
        
    '''
    Sending scheduled message for users that didn't use bot today
    '''

    for user in set(the_users_without_dinner()):
        await bot.send_message(chat_id = user, text = "Хей🖖 не забудь выбрать свой ужин сегодня", reply_markup = menu_garnish)

@dp.message_handler()
async def this_your_dinner_today():
            
    '''
    Sending scheduled message for users that plan their dinner yesterday and inline keyboard to choose if they want to change their choice
    '''

    for id in select_user_dinner_tomorrow():
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        yesterday = yesterday.strftime("%d-%m-%Y")
        if id[1] == yesterday and id[2] != None:
            await bot.send_message(chat_id = id[0], text = f"Привет😀 \nнапомню тебе, что твой ужин сегодня это {id[2]} c {id[3]} и состоится он в {id[4]}. \nХочеш поменять?", reply_markup=inline_yes_no)

@dp.callback_query_handler(text_contains = 'yes')
async def choose_dinner(call:CallbackQuery):
                
    '''
    Accepts the answer, sending reply markup keyboard to choose another dinner
    '''

    await call.answer(cache_time = 60)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('Ти выбрал изменить ужин на сегодня.\nВыбери, что вам по душе сегодня', reply_markup = menu_garnish)
    await call.message.edit_reply_markup(reply_markup = None)

@dp.callback_query_handler(text_contains = 'no')
async def choose_dinner(call:CallbackQuery):
                    
    '''
    Accepts the answer and end the chat
    '''

    await call.answer(cache_time = 60)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('Ты оставил этот ужин\nПриятного аппетита🍽')
    await call.message.edit_reply_markup(reply_markup = None)

    
async def scheduler():
                        
    '''
    Setting the time for sending scheduled message  
    '''

    aioschedule.every().day.at("10:00").do(this_your_dinner_today)
    aioschedule.every().day.at("17:45").do(choose_your_dinner)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
        