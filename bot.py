import asyncio
import handlers
import admin_panel
from loader import dp
import schedul_message
from aiogram import executor
from schedul_message import scheduler
from set_bot_comands import set_default_commands
from database import init_db_user_dinner, init_db_user_dinner_tomorrow


async def on_startup(dp): 
    await set_default_commands(dp)                       # plug in menu button
    asyncio.create_task(scheduler())                     # plug in scheduled messages
    init_db_user_dinner()                                # creating database table
    init_db_user_dinner_tomorrow()                       # creating database table for tomorrow dishes

 
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)    # start the bot
