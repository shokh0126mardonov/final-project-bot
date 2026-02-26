from telegram import InlineKeyboardButton,InlineKeyboardMarkup



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
