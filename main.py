import random

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message


BOT_TOKEN = '7266995394:AAERk5sRQ6wpVF3hz6aK15kRUZLb0JGnCBM'

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()
ATTEMPTS = 5

user = {
    "in_game": False,
    "number": None,
    "attempts": None,
    "total games": 0,
    "wins": 0
}


def get_random_number () -> int:
    return random.randint(0,100)


@dp.message(CommandStart())
async def get_start_info (message: Message):
    await message.answer(
        "Привет! Давай сыграем? Угадаешь загаданное число до 100 за 5 попыток?"
        "Отправь комманду /help, чтобы узнать подробнее"
    )


@dp.message(Command(commands='help'))
async def get_help_info(message: Message):
    await message.answer(
        f'Правила игры:\n\nЯ загадываю число от 1 до 100, '
        f'а вам нужно его угадать\nУ вас есть {ATTEMPS} '
        f'попыток\n\nДоступные команды:\n/help - правила '
        f'игры и список команд\n/cancel - выйти из игры\n'
        f'/stat - посмотреть статистику\n\nДавай сыграем?'
    )


@dp.message(Command(commands='stat'))
async def get_stat_info(message: Message):
    await message.answer(
        f'Всего сыграно игр: {user["total games"]} \n'
        f'Всего побед: {user["wins"]}'
    )

@dp.message(Command(commands='cancel'))
async def get_cancel_info(message: Message):
    if user["in_game"]:
        user["in_game"] = False
        await message.answer(
            "Очень жаль, но ты возвращайся"
        )
    else:
        await message.answer(
            'Мы и не играли:)'
        )

@dp.message(Command(commands='cancel'))
async def get_cancel_info(message: Message):
    if user["in_game"]:
        user["in_game"] = False
        await message.answer(
            "Очень жаль, но ты возвращайся"
        )
    else:
        await message.answer(
            'Мы и не играли:)'
        )

@dp.message(F.text.lower().in_(['да', 'давай', 'сыграем', 'валяй', 'конечно', 'играем', 'игра', 'хочу',]))
async def process_start_game (message: Message):
    if user["in_game"]:
        await message.answer(
            'Мы уже же играем, давай число от 1 до 100'
        )
    else:
        user["in_game"] = True
        user["number"] = get_random_number()
        user["attempts"] = ATTEMPTS
        print (user['attempts'])
        await message.answer(
            'Отлично! \n Я загадал число от 1 до 100'
        )

@dp.message(F.text.lower().in_(['нет', 'не хочу', 'не буду']))
async def process_refuse_game (message: Message):
    if user['in_game']:
        await message.answer(
            'Мы же играем, давай число'
        )
    else:
        await message.answer('Жаль. Если что, жми /start')


@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def process_number_answer (message:Message):
    if user['in_game']:
        if int(message.text) == user['number']:
            user['total games'] +=1
            user['wins'] += 1
            user['in_game'] = False
            await message.answer(
                f'Ты могешь. Это ж победа. Было загадно число {user['number']}'
                )
        elif int(message.text) > user['number']:
            user['attempts'] -= 1
            print (user['attempts'])
            await message.answer(
                'Загаданное число ниже'
                )
        elif int(message.text) < user['number']:
            user['attempts'] -= 1
            print (user['attempts'])
            await message.answer(
                'Загаданное число выше'
                )
        if user['attempts'] == 0:
            print (user['attempts'])
            user['total games'] +=1
            user['in_game'] = False
            await message.answer(
                f'Увы, попытки закончились. Вы проиграли. \n'
                f'Было загадно число {user['number']}'
            )
    else:
        await message.answer('Мы еще не играем. Хотите сыграть?')

# Этот хэндлер будет срабатывать на остальные любые сообщения
@dp.message()
async def process_other_answers(message: Message):
    if user['in_game']:
        await message.answer(
            'Мы же сейчас с вами играем. '
            'Присылайте, пожалуйста, числа от 1 до 100'
        )
    else:
        await message.answer(
            'Я довольно ограниченный бот, давайте '
            'просто сыграем в игру?'
        )

if __name__ == '__main__':
    dp.run_polling(bot)