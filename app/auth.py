from functools import wraps
from aiogram.types import Message
from database.ext.users import get_user_by_id
from server import logger


def auth(command_handler):
    @wraps(command_handler)
    async def handle(message: Message):
        user_id = get_user_by_id(message.from_user.id)
        if not user_id:
            logger.info(f"Message from unauthorised user! ID: {message.from_user.id}")
            return
        if not user_id.is_admin:
            logger.info(f"Message from non-admin user! ID: {message.from_user.id}")
            return
        return await command_handler(message)
    return handle
