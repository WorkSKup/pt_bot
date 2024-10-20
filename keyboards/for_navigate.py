from aiogram import types

keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text='Биржи'),
            types.KeyboardButton(text='Реклама'),
        ],
        [
            types.KeyboardButton(text='Закрытый канал'),
            types.KeyboardButton(text='Менеджер')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите команду'
)

tasks_keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text='check all'),
            types.KeyboardButton(text='add a new task')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Actions...'
)
