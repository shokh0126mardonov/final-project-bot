from telegram import Update,ReplyKeyboardRemove
from telegram.ext import CallbackContext,ConversationHandler

from utils import RegisterStep
from handlers.buttons.auth_buttons import send_contact,confirm_button


def register_handler(update:Update,context:CallbackContext):
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        "Ism-familiyangizni yuboring",
    )

    return RegisterStep.full_name


def get_full_name(update:Update,context:CallbackContext):
    full_name = update.message.text.split()

    if len(full_name) != 2:
        update.message.reply_text("Ism familiyangizni yuboring!")
        return RegisterStep.full_name
    
    context.user_data['chat_id'] = update.effective_user.id
    context.user_data['username'] = update.effective_user.username
 
    context.user_data['first_name'] = full_name[0]
    context.user_data['last_name'] = full_name[1]

    update.message.reply_text(
        "Contactizni yuboring",
        reply_markup=send_contact()
    )

    return RegisterStep.phone_number


def get_phone_number(update:Update,context:CallbackContext):
    context.user_data['contact'] = update.message.contact.phone_number

    update.message.reply_text(
        "Profilingiz uchun rasm yuboring",reply_markup=ReplyKeyboardRemove()
    )

    return RegisterStep.avatar

def get_avatar_image(update: Update, context: CallbackContext):
    file_id = update.message.photo[-1].file_id
    context.user_data['photo'] = file_id

    caption = f"""
        Ma'lumotlaringizni tasdiqlang:

        Ism: {context.user_data['first_name'].title()}
        Familiya: {context.user_data['last_name'].title()}
        Contact: {context.user_data['contact']},
    """

    update.message.reply_photo(
        photo=file_id,
        caption=caption,
        reply_markup=confirm_button()
    )

    return RegisterStep.confirm

def confirm_data(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == "confirm_true":
        query.edit_message_caption(
            caption="Ma'lumotlaringiz tasdiqlandi ✅"
        )
        context.user_data.clear()
        return ConversationHandler.END

    query.edit_message_caption(
        caption="Ism-familiyangizni yuboring:"
        )
    return RegisterStep.full_name