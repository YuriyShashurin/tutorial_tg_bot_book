from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from lexicon.lexicon import LEXICON_RU
from aiogram.filters import Command
from keyboards.main_menu import kb_builder
from aiogram import F


# Инициализируем роутер уровня модуля
router = Router()



@router.message(Command(commands='go'))
async def process_help_command(message: Message):
    await message.answer(text='Любите ли вы домашних животных?',
                         reply_markup=kb_builder.as_markup(resize_keyboard=True,
                                                           one_time_keyboard=True,
                                                           input_field_placeholder='Нажмите кнопку 1'))


@router.message(F.text == 'Да')
async def process_dog_answer(message: Message):
    await message.answer(
        text='Ой, они такие славные',
        # reply_markup=ReplyKeyboardRemove()
    )


# Этот хэндлер будет срабатывать на ответ "Огурцов 🥒" и удалять клавиатуру
@router.message(F.text == 'Нет')
async def process_cucumber_answer(message: Message):
    await message.answer(
        text='Ох, жаль, но ведь они милые',
        # reply_markup=ReplyKeyboardRemove()
    )


@router.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])
