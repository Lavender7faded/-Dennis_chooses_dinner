from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)         # creating your bot and set formatting
storage = MemoryStorage()                                           # specifying state store
dp = Dispatcher(bot, storage=storage)                               # creating handler


# can add logging for working without database

# def log(message):
#     from datetime import datetime
#     dtn = datetime.now()
#     botlogfile = open('TestBot.log', 'a')
#     print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.last_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
#     botlogfile.close()
