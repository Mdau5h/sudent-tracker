import asyncio
import logging
import sys

from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram import Dispatcher
from database.create import rollout as init_db
from app.handlers.start import start_router
from app.handlers.students import students_router
from app.handlers.cancel import cancel_router
from app.config import config

logger = logging.getLogger(__name__)


async def main() -> None:
    bot = Bot(config.TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_routers(
        cancel_router,
        start_router,
        students_router
    )
    init_db()
    logger.info("Database is ready")
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
