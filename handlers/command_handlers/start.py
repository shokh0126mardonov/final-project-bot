import requests

from telegram import Update
from telegram.ext import CallbackContext

from handlers.buttons.auth_buttons import register_button
from utils import settings


def start_bot(update: Update, context: CallbackContext):
    chat_id = update.effective_user.id
    try:
        response = requests.get(
            url=settings.Register_url, params={"chat_id": chat_id}
        ).json()

        if response["status"]:
            update.message.reply_html(
                "🔐 Hisobingiz tayyor.\nDavom etish: <b>/login</b>"
            )
        else:
            update.message.reply_html(
                "📝 <b>Ro‘yxatdan o‘tish</b>\n\n"
                "Tizimdan foydalanish uchun ro‘yxatdan o‘ting 👇",
                reply_markup=register_button(),
            )
    except:
        update.message.reply_text("❌ Kutilmagan xatolik yuz berdi.")
