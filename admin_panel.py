from loader import dp
from config import admin_id
from aiogram.types import Message 
from database import select_all, select_all_tomorrow


@dp.message_handler(user_id = admin_id, commands = ['today'])
async def users_dinner(message:Message):
    
    '''
    Sending message only to admin with dinner from all users from database after writing /today
    '''

    for user in select_all():
        await message.answer(f"На сьогодні {user[2]} {user[3]} о {user[1]} {user[0]} замовив/ла: {user[4]} з {user[5]} на {user[6]}")


@dp.message_handler(user_id = admin_id, commands = ['tomorrow'])
async def users_dinner_tomorrow(message:Message):
        
    '''
    Sending message only to admin with tomorrow dinner from all users from database after writing /tomorrow
    '''

    for user in select_all_tomorrow():
        await message.answer(f"На завтра {user[2]} {user[3]} о {user[1]} {user[0]} замовив/ла: {user[4]} з {user[5]} на {user[6]}")
