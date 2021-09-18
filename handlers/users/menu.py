from loader import dp, bot, log
import datetime
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menu import menu_garnish, menu_entree, menu_time, yes_no, menu_garnish_tomorrow, menu_entree_tomorrow, menu_time_tomorrow
from aiogram.dispatcher.filters import Command, Text
from database import db_table_users_id, db_table_user_dinner, db_table_user_dinner_tomorrow
    

@dp.message_handler(Command('start'))
async def bot_start(message:Message):
    await bot.send_message(message.from_user.id, 'Привет, давай составим твой ужин🤤\nЖмякни /menu')
    log(message)
    
    user_id = message.from_user.id
    try:
        db_table_users_id(user_id = user_id)
    except Exception:
        print(f'{message.from_user.first_name} @{message.from_user.username} повторно заповнює бота')
 

@dp.message_handler(Command('menu'))
async def show_menu(message:Message):
    await message.answer('Выбери какой гарнир хочешь на ужин',
    reply_markup = menu_garnish)
    log(message)
 

@dp.message_handler(Text(equals=['Паста', 'Гречка', 'Кус-кус', 'Чечевица']))
async def get_garnish(message:Message):
    global garnish
    garnish = message.text

    # if garnish == 'Я на диете🙅‍♂️':
    #     await message.answer(f'Ты выбрал {garnish}. Может тогда, что то полегче:',
    #     reply_markup = menu_diet)
    # else:
    await message.answer(f'Ты выбрал {garnish}. \nТеперь выбери что будешь к гарниру', 
    reply_markup = menu_entree)
    log(message)




# @dp.message_handler(Text(equals=['Салат', 'Творог', 'Йогурт', 'Фрукти', 'Обратно к гарниру']))
# async def get_diet(message:Message):
#     global diet
#     diet = message.text
#     if diet == 'Обратно к гарниру':
#         await message.answer(f'Вы вернулись к выбору гарнира',
#         reply_markup = menu_garnish)
        
#     else:
#         await message.answer(f'Ты выбрал {diet}. \nА теперь выбери удобное время',
#         reply_markup = menu_other_time)
        


@dp.message_handler(Text(equals=['Салат', 'Сыр','Тушеные овощи', 'Жареная курица', 'Гарнира хватит вполне👌', 'Обратно к гарниру']))
async def get_entree(message:Message):
    global entree
    entree = message.text
    if entree == 'Обратно к гарниру':
        await message.answer(f'Вы вернулись к выбору гарнира',
        reply_markup = menu_garnish)
    else:
        await message.answer(f'Ты выбрал {entree}. \nА теперь выбери удобное время',
        reply_markup = menu_time)
        log(message)



# @dp.message_handler(Text(equals=['17:00', '18:00', 'Давай сегодня попозже', 'Обратно к меню для диеты']))
# async def get_other_time(message:Message):
#     global other_time
#     other_time = message.text
#     if message.text == 'Обратно к меню для диеты':
#         await message.answer(f'Вы вернулись к выбору диетических блюд',
#         reply_markup = menu_diet)
        
#     else:
#         await message.answer('И так, твой ужин это {} и состоится он {}'.format(diet, other_time),
#         reply_markup=ReplyKeyboardRemove())
        

# @dp.message_handler(Text(equals=['18:00', '19:00', 'Давай сегодня попозже', 'Обратно к основному блюду']))
# async def get_time(message:Message):
#     global time
#     time = message.text
#     if message.text == 'Обратно к основному блюду':
#         await message.answer(f'Вы вернулись к выбору основного блюда',
#         reply_markup = menu_entree)
#     else:
#         await message.answer(f'И так, твой ужин это {garnish} с {entree} и состоится он {time}. \nПриятного аппетита🍽',
#         reply_markup=ReplyKeyboardRemove())
#       


@dp.message_handler(Text(equals=['18:00', '19:00', 'Давай сегодня попозже', 'Обратно к основному блюду']))
async def get_time(message:Message):
    global time
    time = message.text
    if message.text == 'Обратно к основному блюду':
        await message.answer(f'Вы вернулись к выбору основного блюда',
        reply_markup = menu_entree)
    else:
        await message.answer(f'Итак, твой ужин это {garnish} с {entree} и состоится он в {time}.\nПриятного аппетита🍽 \nМожет хочешь составить ужин на завтра?',
        reply_markup = yes_no)
        log(message)

        
        time_now = datetime.datetime.now()

        user_time = time_now.strftime("%d-%m-%Y %H:%M")
        user_id = message.from_user.id
        user_fname = message.from_user.first_name
        user_sname = message.from_user.last_name

        user_gar = garnish
        user_ent = entree
        user_dintime = time

        db_table_user_dinner(time= user_time, user_id = user_id, user_first_name = user_fname, user_surname = user_sname, user_garnish = user_gar,
                        user_entree = user_ent, user_dinner_time = user_dintime)


@dp.message_handler(Text(equals=['Да', 'Нет']))
async def get_yes_no(message:Message):
    yes_no = message.text
    if message.text == 'Да':
        await message.answer('Составим ужин на завтра😋', reply_markup = menu_garnish_tomorrow)
        log(message)
    else:
        await message.answer(f'Не смею задерживать🖐',
        reply_markup = ReplyKeyboardRemove())
        log(message)



@dp.message_handler(Text(equals=['Пюре', 'Рис', 'Булгур']))
async def get_garnish_tomorrow(message:Message):
    global garnish_tomorrow
    garnish_tomorrow = message.text
    await message.answer(f'На завтра ты выбрал {garnish_tomorrow}. \nТеперь выбери что будешь к гарниру', 
    reply_markup = menu_entree_tomorrow)
    log(message)


@dp.message_handler(Text(equals=['Свежие овощи', 'Овощи на пару', 'Легкий салат', 'Мясной соус', 'Гарнира хватит👌', 'Назад к гарниру']))
async def get_entree_tomorrow(message:Message):
    global entree_tomorrow
    entree_tomorrow = message.text
    if entree_tomorrow == 'Назад к гарниру':
        await message.answer(f'Вы вернулись к выбору гарнира',
        reply_markup = menu_garnish_tomorrow)
    else:
        await message.answer(f'На завтра ты выбрал {entree_tomorrow}. \nА теперь выбери удобное время',
        reply_markup = menu_time_tomorrow)
        log(message)

            

@dp.message_handler(Text(equals=['18:30', '19:30', 'Давай попозже', 'Назад к основному блюду']))
async def get_time_tomorrow(message:Message):
    global time_tomorrow
    time_tomorrow = message.text
    if time_tomorrow == 'Назад к основному блюду':
        await message.answer(f'Вы вернулись к выбору основного блюда',
        reply_markup = menu_entree_tomorrow)
    else:
        await message.answer(f'И так, твой ужин на завтра это {garnish_tomorrow} с {entree_tomorrow} и состоится он в {time_tomorrow}.\nПриятного аппетита🍽',
        reply_markup = ReplyKeyboardRemove())
        log(message)
 
        time_now = datetime.datetime.now()

        user_time = time_now.strftime("%d-%m-%Y %H:%M")
        user_id = message.from_user.id
        user_fname = message.from_user.first_name
        user_sname = message.from_user.last_name

        user_gartomorrow = garnish_tomorrow
        user_enttomorrow = entree_tomorrow
        user_dintime_tomorrow = time_tomorrow

        db_table_user_dinner_tomorrow(time= user_time, user_id = user_id, user_first_name = user_fname, user_surname = user_sname, user_garnish_tomorrow = user_gartomorrow, 
                        user_entree_tomorrow = user_enttomorrow, user_dinner_time_tomorrow = user_dintime_tomorrow)

# @dp.message_handler(content_types = ['Да'])
# async def garnish_form_user(message:Message):
#     user_garnish = message.text
#     await bot.send_message(message.from_user.id, f'Составим ужин на завтра😋', reply_markup = menu_garnish)
#   

# @dp.callback_query_handler(text_contains = 'yes')
# async def choose_yes(call:CallbackQuery):
#     await call.answer(cache_time = 60)
#     callback_data = call.data
#     logging.info(f'call = {callback_data}')

#     await call.message.answer('Составим ужин на завтра😋', reply_markup = menu_garnish)

# @dp.callback_query_handler(text_contains = 'no')
# async def choose_yes(call:CallbackQuery):
#     await call.answer(cache_time = 60)
#     callback_data = call.data
#     logging.info(f'call = {callback_data}')

#     await call.message.answer(f'Хорошего ужина🍽', 
#     reply_markup = ReplyKeyboardRemove())
