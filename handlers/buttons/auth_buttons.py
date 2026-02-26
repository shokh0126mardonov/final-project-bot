from telegram import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton



def register_button():
    keyboard = [
        [InlineKeyboardButton(text="Register",callback_data="register_page")]
    ]

    return InlineKeyboardMarkup(keyboard)


def login_button():
    keyboard = [
        [InlineKeyboardButton(text="Login",callback_data="login_page")]
    ]

    return InlineKeyboardMarkup(keyboard)


def send_contact():
    keyboard = [
        [KeyboardButton("contact yuborish",request_contact=True)]
    ]

    return ReplyKeyboardMarkup(
        keyboard,resize_keyboard=True,one_time_keyboard=True
    )


def confirm_button():
    keyboard = [
        [InlineKeyboardButton(text="Tasdiqlash",callback_data="confirm_true"),InlineKeyboardButton(text="Qaytadan",callback_data="confirm_false")]
    ]

    return InlineKeyboardMarkup(keyboard)