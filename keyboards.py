from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button1 = KeyboardButton('/re_Workdirect')
button2 = KeyboardButton('/re_Cleex_back')
button3 = KeyboardButton('/re_Cleex_image')
button4 = KeyboardButton('/re_Kvik_next')
button5 = KeyboardButton('/re_Kvik_image')
markup = ReplyKeyboardMarkup().row(button1, button2, button3)
markup.row(button4, button5)

