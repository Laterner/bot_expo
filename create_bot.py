import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from decouple import config

admins = [] # [int(admin_id) for admin_id in config('ADMINS').split(',')]
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Вынести в конфиг
bot = Bot(token="7730138605:AAH1dUlKRfVb8JlDDMiLRdhtDkLCEow3nYM", default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())
