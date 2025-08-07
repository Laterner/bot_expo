import asyncio
from create_bot import bot, dp, admins
from data_base.base import create_tables
from aiogram.types import BotCommand, BotCommandScopeDefault

from handlers.start_router import start_router

from data_base.dao import get_all_users
from aiohttp import web
import aiohttp_cors


# Функция, которая настроит командное меню (дефолтное для всех пользователей)
async def set_commands():
    commands = [BotCommand(command='start', description='Старт')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


# Функция, которая выполнится когда бот запустится
async def start_bot():
    await set_commands()
    await create_tables()
    for admin_id in admins:
        try:
            await bot.send_message(admin_id, f'Я запущен 🥳.')
        except:
            pass


# Функция, которая выполнится когда бот завершит свою работу
async def stop_bot():
    try:
        for admin_id in admins:
            await bot.send_message(admin_id, 'Бот остановлен.')
    except:
        pass


async def main():
    # регистрация роутеров
    dp.include_router(start_router)

    # регистрация функций
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    # запуск бота в режиме long polling при запуске бот очищает все обновления, которые были за его моменты бездействия
    try:
        await asyncio.gather(
            dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types()),
            start_http_server()
        )
        
    finally:
        await bot.session.close()


async def handle_admin_message(request):
    data = await request.json()
    all_users = await get_all_users()
    text = data.get("text")
    
    if not text:
        return web.json_response({"status": "error", "message": "text required"})
    
    for user in all_users:
        await bot.send_message(user['id'], f"🔔 Сообщение от админа:\n{text}")
    return web.json_response({"status": "ok"})


async def start_http_server():
    app = web.Application()
    app.router.add_post("/admin/send", handle_admin_message)
    runner = web.AppRunner(app)
    
    cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*"
        )
    })
    for route in list(app.router.routes()):
        cors.add(route)
        
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()



if __name__ == "__main__":
    asyncio.run(main())
