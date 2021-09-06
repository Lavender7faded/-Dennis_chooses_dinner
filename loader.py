from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# def log(message):
#     print("<!------!>")
#     from datetime import datetime
#     print(datetime.now())
#     print("Сообщение от {0} {1} (id = {2}) \n {3}".format(message.from_user.first_name,
#                                                               message.from_user.last_name,
#                                                               str(message.from_user.id), message.text))

def log(message):
    from datetime import datetime
    dtn = datetime.now()
    botlogfile = open('TestBot.log', 'a')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.last_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()