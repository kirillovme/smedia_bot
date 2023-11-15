import asyncio

from database.database import get_or_create_user
from loguru import logger
from pyrogram import Client
from pyrogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession


async def message_handler(client: Client, message: Message) -> None:
    """Хендлер всех сообщений пользователя."""
    logger.info(f'Recieved message from user {message.from_user.id}')
    async with AsyncSession(client.db_engine) as session:
        user = await get_or_create_user(session, message.from_user.id)
        if not user:
            logger.info(f'Starting funnel for user {message.from_user.id}')
            asyncio.create_task(send_scheduled_messages(client, message.from_user.id))


async def send_scheduled_messages(client: Client, chat_id: int) -> None:
    """Воронка сообщений для пользователя."""
    await asyncio.sleep(10 * 60)
    logger.info(f'Sending welcome message to {chat_id}')
    await client.send_message(chat_id, 'Добрый день!')
    await asyncio.sleep(90 * 60)
    logger.info(f'Sending materials to {chat_id}')
    await client.send_message(chat_id, 'Подготовила для вас материал')
    await client.send_photo(chat_id, '/bot/img/1.png')
    await asyncio.sleep(2 * 60 * 60)
    async for message in client.get_chat_history(chat_id):
        if 'Хорошего дня' in message.text:
            logger.info(f"Found 'Хорошего дня' in chat history for chat_id: {chat_id}")
            break
    else:
        await client.send_message(chat_id, 'Скоро вернусь с новым материалом!')
        logger.info(f'Sent final message to chat_id: {chat_id}')
