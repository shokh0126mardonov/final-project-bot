import requests

from telegram import Update
from telegram.ext import CallbackContext

from handlers.buttons.auth_buttons import register_button,login_button

Register_url = "http://localhost:8001/user/register/"

def start_bot(update:Update,context:CallbackContext):
    chat_id = update.effective_user.id

    response = requests.get(url=Register_url,params={"chat_id":chat_id})

    if response.json()['exists']:
        update.message.reply_text(
            "Login",reply_markup=login_button()
        )
    else:
        update.message.reply_text(
            "Register",reply_markup=register_button()
        )