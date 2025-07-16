from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery, FSInputFile
from data_base.dao import set_user, get_all_users, get_member_id_by_id
from keyboards.reply_other_kb import main_kb, quest_kb, main_register2
from utils.utils import get_content_info, send_message_user
from create_bot import bot


start_router = Router()

class Form(StatesGroup):
    name = State()  # Состояние для ввода имени

# Хендлер команды /start и кнопки "🏠 Главное меню"
@start_router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    user = None # await cheak_user(tg_id=message.from_user.id,
                        #   username=message.from_user.username,
                        #   full_name=message.from_user.full_name)
    greeting = f"Добро пожаловать, {message.from_user.full_name}! Выбери необходимое действие"
    if user is None:
        greeting = f"Введите своё имя одним словом до 10 символов (так вы будите видны в таблице лидеров)"
        
        await state.set_state(Form.name)
        
        await message.answer(greeting, reply_markup=None)
    else:
        await message.answer(greeting, reply_markup=main_register2())

@start_router.message(F.text == 'Главное меню')
async def main_menu(message: Message, state: FSMContext):
    await state.clear()
    user = await get_member_id_by_id(message.from_user.id)
    print(f'user{message.from_user.id}::', user)
    
    try:
        await message.answer(f'Ваш id:{user['member_id']} \nВаш счёт:{user['score']} \nВоспользуйтесь навигацией внизу экрана',
                            reply_markup=main_register2())
    except Exception as e:
        print('total error::', e)
        await message.answer(f'Выберите необходимое действие.',
                            reply_markup=main_register2())

# Обработчик для сохранения имени
@start_router.message(Form.name)
async def process_name(message: Message, state: FSMContext):
    # Сохраняем имя в состоянии FSM
    await state.update_data(name=message.text)
    
    # Получаем данные из состояния
    data = await state.get_data()
    name = data.get("name", "Неизвестно")
    user = await set_user(tg_id=message.from_user.id,
                          username=message.from_user.username,
                          full_name=name)
    print('user::', user)
    await message.answer(f"\"{name}\", вот мы и познакомились! Вам присвоен уникальный ID {user['member_id']}, запомните его. ID нужен для начисления баллов в квесте. Давайте посмотрим мои возможности. Нажмите кнопку на \"Главное меню\"")
    await state.clear()  # Очищаем состояние





@start_router.message(F.text == 'Регистрация')
async def start_register(message: Message, state: FSMContext):
    await state.clear()
    content_info = get_content_info(message)
    text = f'{message.from_user.full_name}, добро пожаловать на мероприятие ... '
    if content_info.get('content_type'):
        await state.update_data(**content_info)
        await send_message_user(
            bot=bot, 
            content_type=content_info['content_type'], 
            content_text=text,
            user_id=message.from_user.id, 
            kb=main_register2()
        )
        await message.answer('Ваш id:\nВыберите необходимое действие.',
                            reply_markup=main_register2())


@start_router.message(F.text == 'Карта и расписание')
async def start_map(message: Message, state: FSMContext):
    await state.clear()
    text = "12:30 – приветствие \n13:00 – кейтеринг \n13:20 – конкурсы"
    
    # Путь к файлу относительно корня проекта
    photo_path = "map.jpg"
    
    # Создаем объект файла
    photo = FSInputFile(photo_path)
    
    await message.answer_photo(
        photo=photo,
        caption=text,
        reply_markup=main_register2()
    )

@start_router.message(F.text == 'FAQ')
async def start_faq(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Все вопросы можете задать сюда: @Ivangogis',
                        reply_markup=main_register2())   


@start_router.message(F.text == 'Таблица лидеров')
async def start_faq(message: Message, state: FSMContext):
    await state.clear()
    users = await get_all_users()
    # print("users::::::::", users)
    str_val = ""
    for user in users:
        # print("user::::::::", user)
        str_val += f"{user['full_name']} {user['member_id']} {user['score']} \n"
    await message.answer('10 лучших частников: \n' + str_val,
                        reply_markup=main_register2())   



@start_router.message(F.text == 'DeleteDataBase')
async def stop_fsm(message: Message, state: FSMContext):
    await state.clear()
    # await delete_all_users()
    await message.answer(f"Сценарий остановлен. Для выбора действия воспользуйся клавиатурой ниже",
                        reply_markup=main_register2())

@start_router.message(F.text == 'Квест')
async def quest_0(message: Message, state: FSMContext):
    await state.clear()
    text = "12:30 – приветствие \n13:00 – кейтеринг \n13:20 – конкурсы"
    
    # Путь к файлу относительно корня проекта
    photo_path = "map.jpg"
    
    # Создаем объект файла
    photo = FSInputFile(photo_path)
    
    await message.answer(text, reply_markup=quest_kb())

@start_router.message(F.text == 'Квест')
async def quest_0(message: Message, state: FSMContext):
    await state.clear()
    text = "Это список квестов"
    
    await message.answer(text, reply_markup=quest_kb())

@start_router.message(F.text == 'Квест 1')
async def quest_1(message: Message, state: FSMContext):
    await state.clear()
    text = "Это описание квеста 1"
    
    await message.answer(text, reply_markup=quest_kb())

@start_router.message(F.text == 'Квест 2')
async def quest_2(message: Message, state: FSMContext):
    await state.clear()
    text = "Это описание квеста 2"
    
    await message.answer(text, reply_markup=quest_kb())
    
@start_router.callback_query(F.data == 'main_menu')
async def main_menu_process(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.answer('Вы вернулись в главное меню.')
    await call.message.answer(f"Привет, {call.from_user.full_name}! Выбери необходимое действие",
                              reply_markup=main_register2())
