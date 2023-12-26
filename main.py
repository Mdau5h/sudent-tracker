import asyncio
import logging
import sys

from aiogram import Bot
from aiogram.enums import ParseMode
from app.handlers import dp
from app.config import config


async def main() -> None:
    bot = Bot(config.TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
