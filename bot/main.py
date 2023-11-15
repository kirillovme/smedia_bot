import asyncio

from config.config import TELEGRAM_API_HASH, TELEGRAM_API_ID
from database.database import init_db
from handlers.handlers import message_handler
from loguru import logger
from pyrogram import Client, filters, handlers


async def main():
    """Точка входа в бота."""
    app = Client(
        'my_account',
        api_id=TELEGRAM_API_ID,
        api_hash=TELEGRAM_API_HASH
    )
    engine = await init_db()
    app.db_engine = engine
    await app.start()
    app.add_handler(handlers.MessageHandler(message_handler, filters.text))
    idle_event = asyncio.Event()
    try:
        logger.info('Starting bot...')
        await idle_event.wait()
    finally:
        await app.stop()


if __name__ == '__main__':
    asyncio.run(main())
