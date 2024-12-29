from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет')
    await message.reply('Как дела?')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Ты нажал на кнопку помощи. Бла бла хз что писать')

@router.message(F.text == 'Скажи триста')
async def hui(message: Message):
    await message.answer('Отсоси у тракториста')

@router.message(Command('Картинка'))
async def send_mem(message: Message):
    photo_url = 'https://www.amic.ru/images/news/webp/555042_size1.webp'
    await message.answer_photo(photo_url)

@router.message(F.photo)
async def save_photo(message: Message):
    photo = message.photo
    file = photo.file_id
    file_path = f'cash/{file}.jpg'
    new_file = await message.bot.get_file(file)
    await message.bot.download_file(new_file.file_path, file_path)
    await message.answer('Фото сохранено')