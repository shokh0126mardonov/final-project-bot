from telegram.ext import Updater,CommandHandler,MessageHandler,ConversationHandler,Filters,CallbackQueryHandler

from handlers.command_handlers import start_bot
from handlers.message_handlers import register_handler
from utils import settings

def main():
    updater = Updater(token=settings.TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start",start_bot))   

    register = ConversationHandler(
        entry_points=[dispatcher.add_handler(
            MessageHandler(Filters("register_page"),
            callback=register_handler)
        )
    ],

        states={
            
        },
        fallbacks=[],
    )
    dispatcher.add_handler(register)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()