from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def generate_date_keyboard(notes):
    unique_dates = {note['date_created'].strftime('%Y-%m-%d') for note in notes}
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    for date_create in unique_dates:
        button = InlineKeyboardButton(text=date_create, callback_data=f"date_note_{date_create}")
        keyboard.inline_keyboard.append([button])

    keyboard.inline_keyboard.append([InlineKeyboardButton(text="Главное меню", callback_data="main_menu")])

    return keyboard


def generate_type_content_keyboard(notes):
    unique_content = {note['content_type'] for note in notes}
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    for content_type in unique_content:
        button = InlineKeyboardButton(text=content_type, callback_data=f"content_type_note_{content_type}")
        keyboard.inline_keyboard.append([button])

    keyboard.inline_keyboard.append([InlineKeyboardButton(text="Главное меню", callback_data="main_menu")])

    return keyboard

