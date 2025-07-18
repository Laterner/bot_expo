from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


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
