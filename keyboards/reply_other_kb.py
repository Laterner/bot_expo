from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def main_register():
    kb_list = [
        [KeyboardButton(text="Регистрация")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )

def main_kb():
    kb_list = [
        # [KeyboardButton(text="Главное меню")],
        [KeyboardButton(text="Карта и расписание")],
        [KeyboardButton(text="Таблица лидеров")],
        [KeyboardButton(text="Квест")],
        [KeyboardButton(text="FAQ")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )
    
def main_kb_2():
    kb_list = [
        [KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )

def legend_kb():
    kb_list = [
        [KeyboardButton(text="Станции с описанием")],
        [KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )
    
def statuion_kb():
    kb_list = [
        [KeyboardButton(text="Легенда и правила")],
        [KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )

def map_kb():
    kb_list = [
        [KeyboardButton(text="Запись на МАСТЕР-КЛАСС")],
        [KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )
    
def quest_kb():
    kb_list = [
        [KeyboardButton(text="Легенда и правила")],
        [KeyboardButton(text="Станции с описанием")],
        [KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )

def quest_kb_2():
    kb_list = [
        [KeyboardButton(text="Станции с описанием")],
        [KeyboardButton(text="Главное меню")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )
    
def stop_fsm():
    kb_list = [
        [KeyboardButton(text="❌ Остановить сценарий")],
        [KeyboardButton(text="🏠 Главное меню")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Для того чтоб остановить сценарий FSM нажми на одну из двух кнопок👇"
    )

def ease_link_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text="1", callback_data="stations_info")],
        [InlineKeyboardButton(text="2", callback_data="stations_info")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def create_qst_inline_kb(questions: dict) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    # Добавляем кнопки вопросов
    for question_id, question_data in questions.items():
        builder.row(
            InlineKeyboardButton(
                text=question_data.get('qst'),
                callback_data=f'qst_{question_id}'
            )
        )
    # Добавляем кнопку "На главную"
    builder.row(
        InlineKeyboardButton(
            text='На главную',
            callback_data='back_home'
        )
    )
    # Настраиваем размер клавиатуры
    builder.adjust(1)
    return builder.as_markup()