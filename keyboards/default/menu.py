from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.default.callback_datas import choos_callback

yes_no = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да'),
            KeyboardButton(text='Нет'),
        ]
    ],
    resize_keyboard = True
)

menu_garnish = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = 'Паста'),
            KeyboardButton(text = 'Гречка')
        ],
        [
            KeyboardButton(text = 'Чечевица'),
            KeyboardButton(text = 'Кус-кус')
        ],
    ],
    resize_keyboard = True
)
# menu_diet = ReplyKeyboardMarkup(
# keyboard = [
#     [
#         KeyboardButton(text = 'Салат'),
#         KeyboardButton(text = 'Творог')
#     ],
#     [
#         KeyboardButton(text = 'Йогурт'),
#         KeyboardButton(text = 'Фрукти')
#     ],
#     [
#         KeyboardButton(text = 'Обратно к гарниру')
#     ],
# ],
# resize_keyboard = True
# )
menu_entree = ReplyKeyboardMarkup(
keyboard = [
    [
        KeyboardButton(text = 'Салат'),
        KeyboardButton(text = 'Сыр')
    ],
    [
        KeyboardButton(text = 'Тушеные овощи'),
        KeyboardButton(text = 'Жареная курица')
    ],
    [
        KeyboardButton(text = 'Гарнира хватит вполне👌'),
         KeyboardButton(text = 'Обратно к гарниру')
    ],
],
resize_keyboard = True
)

# menu_other_time = ReplyKeyboardMarkup(
# keyboard = [
#     [
#         KeyboardButton(text = '17:00')
#     ],
#     [        
#         KeyboardButton(text = '18:00')
#     ],
#     [
#         KeyboardButton(text = 'Давай сегодня попозже'),
#         KeyboardButton(text = 'Обратно к меню для диеты')
#     ],
    
# ],
#     resize_keyboard = True
# )
menu_time = ReplyKeyboardMarkup(
keyboard = [
    [
        KeyboardButton(text = '18:00')
    ],
    [        
        KeyboardButton(text = '19:00')
    ],
    [
        KeyboardButton(text = 'Давай сегодня попозже'),
        KeyboardButton(text = 'Обратно к основному блюду')
    ],
    
],
    resize_keyboard = True
)

menu_garnish_tomorrow = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = 'Пюре'),
            KeyboardButton(text = 'Рис')
        ],
        [
            KeyboardButton(text = 'Булгур')
        ],
    ],
    resize_keyboard = True
)

menu_entree_tomorrow = ReplyKeyboardMarkup(
keyboard = [
    [
        KeyboardButton(text = 'Свежие овощи'),
        KeyboardButton(text = 'Овощи на пару')
    ],
    [
        KeyboardButton(text = 'Легкий салат'),
        KeyboardButton(text = 'Мясной соус')
    ],
    [
        KeyboardButton(text = 'Гарнира хватит👌'),
         KeyboardButton(text = 'Назад к гарниру')
    ],
],
resize_keyboard = True
)

menu_time_tomorrow = ReplyKeyboardMarkup(
keyboard = [
    [
        KeyboardButton(text = '18:30')
    ],
    [        
        KeyboardButton(text = '19:30')
    ],
    [
        KeyboardButton(text = 'Давай попозже'),
        KeyboardButton(text = 'Назад к основному блюду')
    ],
    
],
    resize_keyboard = True
)