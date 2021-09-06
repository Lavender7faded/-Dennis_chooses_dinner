from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

yes_no = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Да', callback_data=),
            InlineKeyboardButton(text='Нет', callback_data=)

        ]
    ]
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