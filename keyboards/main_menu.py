from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types.web_app_info import WebAppInfo



# button_1 = KeyboardButton(text='Кнопка 1')
# button_2 = KeyboardButton(text='Кнопка 2')
# button_3 = KeyboardButton(text='Кнопка 3')
# button_4 = KeyboardButton(text='Кнопка 4')
# button_5 = KeyboardButton(text='Кнопка 5')
# button_6 = KeyboardButton(text='Кнопка 6')
# button_7 = KeyboardButton(text='Кнопка 7')
# button_8 = KeyboardButton(text='Кнопка 8')
# button_9 = KeyboardButton(text='Кнопка 9')


# # Генерируем список с кнопками
# buttons: list[KeyboardButton] = [
#     KeyboardButton(text=f'Кнопка {i}') for i in range(1, 10)]

# # Составляем список списков для будущей клавиатуры
# keyboard: list[list[KeyboardButton]] = [
#     [buttons[0]],
#     buttons[1:3],
#     buttons[3:6],
#     buttons[6:8],
#     [buttons[8]]
# ]

# keyboard = ReplyKeyboardMarkup(
#     keyboard=keyboard,
#     # keyboard=[[button_1, button_2, button_3],
#     #           [button_4, button_5, button_6],
#     #           [button_7, button_8, button_9]],
#     resize_keyboard=True
# )

kb_builder = ReplyKeyboardBuilder()
# buttons: list[KeyboardButton] = [
#     KeyboardButton(text=f'Кнопка {i + 1}') for i in range(10)
# ]

# kb_builder.row(*buttons, width=4)

# kb_builder.adjust(1, 3)

# Создаем кнопки
contact_btn = KeyboardButton(
    text='Отправить телефон',
    request_contact=True
)
geo_btn = KeyboardButton(
    text='Отправить геолокацию',
    request_location=True
)
poll_btn = KeyboardButton(
    text='Создать опрос/викторину',
    request_poll=KeyboardButtonPollType()
)
# Создаем кнопку
web_app_btn = KeyboardButton(
    text='Start Web App',
    web_app=WebAppInfo(url="https://stepik.org/")
)
# Добавляем кнопки в билдер
kb_builder.row(contact_btn, geo_btn, poll_btn,web_app_btn, width=1)
