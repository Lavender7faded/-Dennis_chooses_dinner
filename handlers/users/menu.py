from loader import dp, bot, log
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menu import menu_garnish, menu_entree, menu_time, menu_diet
from aiogram.dispatcher.filters import Command, Text


@dp.message_handler(Command('start'))
async def cmd_start(message:Message):
    await bot.send_message(message.from_user.id, 'Привет, давай составим твой ужин🤤\nЖмякни /menu')
    log(message)

@dp.message_handler(Command('menu'))
async def show_menu(message:Message):
    await message.answer('Выбери какой гарнир хочешь на ужин',
    reply_markup = menu_garnish)
    log(message)

@dp.message_handler(Text(equals=['Паста', 'Гречка', 'Кус-кус', 'Чечевица', 'Я на диете🙅‍♂️']))
async def get_garnish(message:Message):
    global garnish
    garnish = message.text
    if garnish == 'Я на диете🙅‍♂️':
        await message.answer(f'Ты выбрал {garnish}. Может тогда, что то полегче:',
        reply_markup = menu_diet)
        log(message) 
    else:
        await message.answer(f'Ты выбрал {garnish}. \nТеперь выбери что будешь к гарниру', 
        reply_markup = menu_entree)
        log(message)


@dp.message_handler(Text(equals=['Салат', 'Творог', 'Йогурт', 'Фрукти', 'Обратно к гарниру']))
async def get_diet(message:Message):
    global diet
    diet = message.text
    if diet == 'Обратно к гарниру':
        await message.answer(f'Вы вернулись к выбору гарнира',
        reply_markup = menu_garnish)
        log(message)
    else:
        await message.answer(f'Ты выбрал {diet}. \nА теперь выбери удобное время',
        reply_markup = menu_time_diet)
        log(message)

@dp.message_handler(Text(equals=['Салат', 'Сыр','Тушеные овощи', 'Жареная курица', 'Гарнира хватит вполне👌', 'Обратно к гарниру']))
async def get_entree(message:Message):
    global entree
    entree = message.text
    await message.answer(f'Ты выбрал {entree}. \nА теперь выбери удобное время',
    reply_markup = menu_time)
    log(message)

@dp.message_handler(Text(equals=['18:00', '19:00', 'Давай сегодня попозже', 'Обратно к основному блюду']))
async def get_time(message:Message):
    global time
    time = message.text
    if message.text == 'Обратно к основному блюду':
        await message.answer(f'Вы вернулись к выбору основного блюда',
        reply_markup = menu_entree)
        log(message)
    else:
        await message.answer('И так, твой ужин это {} с {} и состоится он {}'.format(garnish, entree, time),
        reply_markup=ReplyKeyboardRemove())
        log(message)