from aiogram import types


async def set_default_commands(dp):

    '''
    Creating menu with all needed command for users
    '''

    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запуск бота"),
            types.BotCommand("menu", "Показать меню")
        ]
    )