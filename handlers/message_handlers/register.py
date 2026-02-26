import requests

from telegram import Update,ReplyKeyboardRemove
from telegram.ext import CallbackContext,ConversationHandler

from utils import RegisterStep,settings
from handlers.buttons.auth_buttons import send_contact,confirm_button


def register_handler(update:Update,context:CallbackContext):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        "📝 <b>Ro‘yxatdan o‘tish</b>\n\n"
        "Iltimos, <b>ism</b> va <b>familiyangizni</b> kiriting.\n"
        "Masalan: <code>Ali Valiyev</code>",
        parse_mode="HTML"
    )

    return RegisterStep.full_name


def get_full_name(update:Update,context:CallbackContext):
    full_name = update.message.text.split()

    if len(full_name) != 2:
        update.message.reply_html(
            "❗ <b>Xatolik</b>\n\n"
            "Iltimos, ism va familiyangizni to‘liq kiriting.\n"
            "Masalan: <code>Ali Valiyev</code>"
        )       
        return RegisterStep.full_name
 
    context.user_data['first_name'] = full_name[0].title()
    context.user_data['last_name'] = full_name[1].title()

    update.message.reply_html(
    "📱 <b>Telefon raqam</b>\n\n"
    "Quyidagi tugma orqali kontaktingizni yuboring 👇",
    reply_markup=send_contact()
)

    return RegisterStep.phone_number


def get_phone_number(update:Update,context:CallbackContext):
    context.user_data['contact'] = update.message.contact.phone_number

    update.message.reply_html(
    "🖼 <b>Profil rasmi</b>\n\n"
    "Profilingiz uchun rasm yuboring.",
    reply_markup=ReplyKeyboardRemove()
    )

    return RegisterStep.avatar

def get_avatar_image(update: Update, context: CallbackContext):

    file_id = update.message.photo[-1].file_id
    file = context.bot.get_file(file_id)
    photo_url = file.file_path

    context.user_data['photo_url'] = photo_url

    caption = (
    "📋 <b>Ma'lumotlaringizni tasdiqlang</b>\n\n"
    f"👤 <b>Ism:</b> {context.user_data['first_name']}\n"
    f"👤 <b>Familiya:</b> {context.user_data['last_name']}\n"
    f"📱 <b>Telefon:</b> {context.user_data['contact']}\n\n"
    "Ma'lumotlar to‘g‘rimi?"
    )

    update.message.reply_photo(
        photo=file_id,
        caption=caption,
        reply_markup=confirm_button(),
        parse_mode="HTML"
    )

    return RegisterStep.confirm

def confirm_data(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == "confirm_true":

        data = {
            "chat_id" : update.effective_user.id,
            "username" :update.effective_user.username,
            "first_name":  context.user_data['first_name'],
            "last_name" : context.user_data['last_name'],
            "contact": context.user_data['contact'],
            "photo_url":context.user_data['photo_url']
            }

        

        response = requests.post(
            settings.Register_url,
            data=data,
            timeout=5
        )
        query.edit_message_caption(
        caption=(
            "✅ <b>Ma'lumotlaringiz tasdiqlandi!</b>\n\n"
            "Ro‘yxatdan o‘tish muvaffaqiyatli yakunlandi 🎉"
            ),
            parse_mode="HTML"
        )

        context.user_data.clear()
        return ConversationHandler.END

    query.edit_message_caption(
    caption=(
        "🔁 <b>Qayta kiritish</b>\n\n"
        "Iltimos, ism va familiyangizni qayta yuboring.\n"
        "Masalan: <code>Ali Valiyev</code>"
    ),
    parse_mode="HTML"
    )

    return RegisterStep.full_name