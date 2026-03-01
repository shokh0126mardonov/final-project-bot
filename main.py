from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    Filters,
    CallbackQueryHandler,
)

from handlers.command_handlers import start_bot,help_bot
from handlers.message_handlers import (
    register_handler,
    get_avatar_image,
    get_full_name,
    get_phone_number,
    confirm_data,
    login_page
)
from utils import settings, RegisterStep


def main():
    updater = Updater(token=settings.TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_bot))
    dispatcher.add_handler(CommandHandler("help", help_bot))
    dispatcher.add_handler(CommandHandler("login", login_page))

    dispatcher.add_handler(CallbackQueryHandler(login_page,pattern=r"^login_page$"))


    register = ConversationHandler(
        entry_points=[
            CallbackQueryHandler(register_handler, pattern=r"^register_page$")
        ],
        states={
            RegisterStep.full_name: [
                MessageHandler(Filters.text & ~Filters.command, get_full_name)
            ],
            RegisterStep.phone_number: [
                MessageHandler(Filters.contact, get_phone_number)
            ],
            RegisterStep.avatar: [
                MessageHandler(Filters.photo, get_avatar_image)
            ],
            RegisterStep.confirm: [
                CallbackQueryHandler(confirm_data, pattern=r"^confirm_")
            ]
                    },
        fallbacks=[],
    )

    dispatcher.add_handler(register)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()