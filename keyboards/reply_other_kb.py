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

def main_register2():
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
    
def main_kb():
    kb_list = [
        [KeyboardButton(text="📝 Заметки")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )

def quest_kb():
    kb_list = [
        [KeyboardButton(text="Квест 1")],
        [KeyboardButton(text="Квест 2")],
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
