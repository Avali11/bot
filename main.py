import asyncio
from aiogram import Bot, Dispatcher, F

from app.handlers import router
from app.config import ip_adress, datebase, token

async def main():
    bot = Bot(token='7565965621:AAFHPUqsxdf9sbnxKesx8HEnugwiTxv65qQ')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот завершён')