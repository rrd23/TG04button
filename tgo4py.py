import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from config import TOKEN
import keyboards as kb


bot = Bot(token=TOKEN)

dp = Dispatcher()

@dp.message(F.text == "Привет")
async def test_button(message: Message):
   await message.answer(f'Привет, {message.from_user.full_name}!')

@dp.message(F.text == "Пока")
async def test_button(message: Message):
   await message.answer(f'Пока, {message.from_user.full_name}!')

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет! Выберите опцию:", reply_markup=kb.main)


@dp.message(Command("list" ))
async def list(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup = kb.inlinekeyboard_test)



@dp.message(Command("dynamic" ))
async def dynamic(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup = kb.inlinekeyboard_test1)




@dp.callback_query(F.data == "Options")
async def options(callback: CallbackQuery):
   await callback.message.edit_text(text='Вот ваши опции', reply_markup = await kb.test_keyboard())


# Обработчик нажатий на кнопки "Опция 1" и "Опция 2"
@dp.callback_query(F.data.startswith("option_"))
async def option_selected(callback: CallbackQuery):
    # Извлекаем название опции из callback_data
    option = callback.data.split('_')[1]
    # Отправляем сообщение с текстом опции
    await callback.message.answer(f"Вы выбрали {option}")






async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())