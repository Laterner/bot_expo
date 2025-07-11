from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from data_base.dao import set_user, get_all_users
from keyboards.reply_other_kb import main_kb, main_register, main_register2
from utils.utils import get_content_info, send_message_user
from create_bot import bot


start_router = Router()


# Хендлер команды /start и кнопки "🏠 Главное меню"
@start_router.message(F.text == 'Главное меню')
@start_router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    user = await set_user(tg_id=message.from_user.id,
                          username=message.from_user.username,
                          full_name=message.from_user.full_name)
    greeting = f"Добро пожаловать, {message.from_user.full_name}! Выбери необходимое действие"
    if user is None:
        greeting = f"Приветствуем, новый пользователь! Выбери необходимое действие"
        await message.answer(greeting, reply_markup=main_register())
    else:
        await message.answer(greeting, reply_markup=main_register2())



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
        await message.answer('Выберите необходимое действие.',
                            reply_markup=main_register2())


@start_router.message(F.text == 'Карта и расписание')
async def start_map(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('*Здесь будет карта* \n12:30 – приветствие \n13:00 – кейтеринг \n13:20 – конкурсы ',
                        reply_markup=main_register2())

@start_router.message(F.text == 'FAQ')
async def start_faq(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Все вопросы можете задать сюда: @laterner',
                        reply_markup=main_register2())   


@start_router.message(F.text == 'Таблица лидеров')
async def start_faq(message: Message, state: FSMContext):
    await state.clear()
    users = await get_all_users()
    # print("users::::::::", users)
    str_val = ""
    for user in users:
        # print("user::::::::", user)
        str_val += f"{user['member_id']} | {user['full_name']} | {user['score']} \n"
    await message.answer('10 лучших частников: \n' + str_val,
                        reply_markup=main_register2())   



@start_router.message(F.text == '❌ Остановить сценарий')
async def stop_fsm(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(f"Сценарий остановлен. Для выбора действия воспользуйся клавиатурой ниже",
                        reply_markup=main_register2())


@start_router.callback_query(F.data == 'main_menu')
async def main_menu_process(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.answer('Вы вернулись в главное меню.')
    await call.message.answer(f"Привет, {call.from_user.full_name}! Выбери необходимое действие",
                              reply_markup=main_register2())
