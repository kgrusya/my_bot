import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import user_handlers, other_handlers
from keyboards.set_menu import set_main_menu

# Инициализируем логгер
logger = logging.getLogger(__name__)


async def main():
    #  Конфигурируем логер
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )
    # Выводим инфу в терминал, что запустили бота
    logging.info("Starting bot")

    # Инициализируем конфиг
    config: Config = load_config()

    # Инициализируем бота и диспетчер
    bot = Bot(token=config.tg_bot.token,
              parse_mode="HTML")
    dp = Dispatcher()

    # Регистрируем роутеры в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропускаем накопившеся апдейти и запускам polling
    await set_main_menu(bot)
    await bot.delete_webhook(drop_pending_updates=True) 
    await dp.start_polling(bot)

asyncio.run(main())
    

