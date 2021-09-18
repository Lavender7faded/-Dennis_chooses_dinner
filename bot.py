from aiogram import executor
import asyncio
import aioschedule
from database import init_db_user_dinner, init_db_users_id, init_db_user_dinner_tomorrow, select_users_id
import handlers


from loader import dp, bot
# from utils.notify_admins import on_startup_notify
from set_bot_comands import set_default_commands

@dp.message_handler()
async def choose_our_dinner():
    for id in select_users_id():
        await bot.send_message(chat_id = id, text = "Хей🖖 не забудь выбрать свой ужин сегодня")
@dp.message_handler()
async def this_is_our_dinner():
    for id in select_users_id():
        await bot.send_message(chat_id = id, text = "")


async def scheduler():
    aioschedule.every().day.at("10:00").do(this_is_our_dinner)
    aioschedule.every().day.at("17:01").do(choose_our_dinner)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def on_startup(dp):
    # Устанавливаем дефолтные команды
    await set_default_commands(dp)
    asyncio.create_task(scheduler())
    init_db_user_dinner()
    init_db_user_dinner_tomorrow()
    init_db_users_id()

    # # Уведомляет про запуск
    # await on_startup_notify(dp)


 
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
