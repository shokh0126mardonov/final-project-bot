from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
)


def register_button():
    keyboard = [
        [
            InlineKeyboardButton(
                text="📝 Ro‘yxatdan o‘tish", callback_data="register_page"
            )
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


# def login_button():
#     keyboard = [
#         [InlineKeyboardButton(text="🔐 Tizimga kirish", callback_data="login_page")]
#     ]
#     return InlineKeyboardMarkup(keyboard)


def send_contact():
    keyboard = [[KeyboardButton("📱 Telefon raqamni yuborish", request_contact=True)]]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)


def confirm_button():
    keyboard = [
        [
            InlineKeyboardButton(text="✅ Tasdiqlash", callback_data="confirm_true"),
            InlineKeyboardButton(
                text="🔄 Qayta kiritish", callback_data="confirm_false"
            ),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
