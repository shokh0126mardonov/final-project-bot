from telegram.ext import CallbackContext
from telegram import Update


def help_bot(update: Update, context: CallbackContext):
    update.message.reply_html(
        text=(
            "📌 <b>Yordam va Takliflar</b>\n\n"
            "Agar bot bilan bog‘liq <b>muammo</b> yoki "
            "<b>takliflaringiz</b> bo‘lsa,\n\n"
            "👉 <a href='https://t.me/shokhjahon_0126'>@shokhjahon_0126</a> "
            "ga murojaat qiling.\n\n"
            "⏳ Tez orada javob beriladi."
        )
    )