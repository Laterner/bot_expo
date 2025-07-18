from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery, FSInputFile
from data_base.dao import set_user, get_all_users, get_user_by_id
from keyboards.reply_other_kb import *
from utils.utils import get_content_info, send_message_user
from create_bot import bot


start_router = Router()

class Form(StatesGroup):
    name = State()  # Состояние для ввода имени

def call_answer_file(name: str) -> str:
    text = "Не удалось загрузить"
    
    with open(f'./temp_answers/{name}', 'r', encoding='utf-8') as f:
        text = f.read()
    return text

@start_router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    user = None # await cheak_user(tg_id=message.from_user.id,
                        #   username=message.from_user.username,
                        #   full_name=message.from_user.full_name)
    greeting = f"Добро пожаловать, {message.from_user.full_name}! Выбери необходимое действие"
    # if user is None:
    #     ans = call_answer_file('start')
        
        
    #     await message.answer(ans, reply_markup=main_register)
    # else:
    #     await message.answer(greeting, reply_markup=main_kb())
    ans = call_answer_file('start')    
    await message.answer(ans, reply_markup=main_register())

@start_router.message(F.text == 'Главное меню')
async def main_menu(message: Message, state: FSMContext):
    await state.clear()
    user = await get_user_by_id(message.from_user.id)
    print(f'user{message.from_user.id}::', user)
    
    try:
        await message.answer(f'Твой id: {user['member_id']} \nТвой счёт: {user['score']} \nВоспользуйся навигацией внизу экрана',
                            reply_markup=main_kb())
    except Exception as e:
        print('total error::', e)
        await message.answer(f'Твой id: 0000 \nТвой счёт: 0',
                            reply_markup=main_kb())

# Обработчик для сохранения имени
@start_router.message(Form.name)
async def process_name(message: Message, state: FSMContext):
    # Сохраняем имя в состоянии FSM
    await state.update_data(name=message.text)
    
    # Получаем данные из состояния
    data = await state.get_data()
    name = data.get("name", "Неизвестно")
    user_id = await set_user(tg_id=message.from_user.id,
                          username=message.from_user.username,
                          full_name=name)
    # print('user::', user)
    ans = f"{name}, вот мы и познакомились! \n Тебе присвоен уникальный ID {user_id} , запомни его!\nID нужен для зачисления баллов в квесте. \nДавай посмотрим мои возможности. Нажми кнопку \"Главное меню\""
    
    await message.answer(ans, reply_markup=main_kb_2())
    await state.clear()  # Очищаем состояние


@start_router.message(F.text == 'Регистрация')
async def start_register(message: Message, state: FSMContext):
    await state.clear()
    ans = f"Введите своё имя одним словом до 10 символов (так вы будите видны в таблице лидеров)"
    
    await state.set_state(Form.name)
    await message.answer(ans,
        reply_markup=None)


@start_router.message(F.text == 'Карта и расписание')
async def start_map(message: Message, state: FSMContext):
    await state.clear()
    
    text = call_answer_file('rasp')
    
    # Путь к файлу относительно корня проекта
    photo_path = "map.jpg"
    
    # Создаем объект файла
    photo = FSInputFile(photo_path)
    
    await message.answer_photo(
        photo=photo,
        caption=text,
        reply_markup=map_kb()
    )

@start_router.message(F.text == 'Легенда и правила')
async def start_legends(message: Message, state: FSMContext):
    await state.clear()
    text = call_answer_file('legends')
    await message.answer(text,
                        reply_markup=legend_kb())

@start_router.message(F.text == 'Станции с описанием')
async def start_stations(message: Message, state: FSMContext):
    await state.clear()
    text = call_answer_file('rasp')
    await message.answer(text,
                        reply_markup=statuion_kb())
    
@start_router.message(F.text == 'FAQ')
async def start_faq(message: Message, state: FSMContext):
    await state.clear()
    ans = call_answer_file('faq')
    await message.answer(ans,
                        reply_markup=main_kb_2())   


@start_router.message(F.text == 'Таблица лидеров')
async def start_table(message: Message, state: FSMContext):
    await state.clear()
    users = await get_all_users()
    # print("users::::::::", users)
    str_val = ""
    for user in users:
        # print("user::::::::", user)
        str_val += f"{user['full_name']} | {user['member_id']} | {user['score']} \n"
    await message.answer('30 лучших участников: \n' + str_val + "Не нашли себя? Возможно, вы не в топ-30.",
                        reply_markup=main_kb_2())   



# @start_router.message(F.text == 'DeleteDataBase')
# async def stop_fsm(message: Message, state: FSMContext):
#     await state.clear()
#     # await delete_all_users()
#     await message.answer(f"Сценарий остановлен. Для выбора действия воспользуйся клавиатурой ниже",
#                         reply_markup=main_kb())


@start_router.message(F.text == 'Квест')
async def quest_0(message: Message, state: FSMContext):
    await state.clear()
    text = "Это список квестов"
    
    await message.answer(text, reply_markup=quest_kb())

# @start_router.callback_query(F.data == 'main_menu')
# async def main_menu_process(call: CallbackQuery, state: FSMContext):
#     await state.clear()
#     # await call.answer('Вы вернулись в главное меню.')
#     await call.message.answer(f"Воспользуйся навигацией внизу экрана",
#                               reply_markup=main_kb())
