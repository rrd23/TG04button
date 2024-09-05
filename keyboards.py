from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Привет')],
    [KeyboardButton(text='Пока')]

], resize_keyboard=True)

inlinekeyboard_test = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='News', url='https://youtu.be/dQw4w9WgXcQ')],
    [InlineKeyboardButton(text='Music', url='https://youtu.be/dQw4w9WgXcQ')],
    [InlineKeyboardButton(text='Video', url='https://youtu.be/dQw4w9WgXcQ')]

])

inlinekeyboard_test1 = InlineKeyboardMarkup(inline_keyboard=[

    [InlineKeyboardButton(text='Показать больше', callback_data='Options')]

])

test = ["опция 1", "опция 2", ]


async def test_keyboard():
    keyboard = InlineKeyboardBuilder()
    for key in test:
        keyboard.add(InlineKeyboardButton(text=key, callback_data=f'option_{key}'))
    return keyboard.adjust(2).as_markup()
