import random
import redis
import random

from telegram import Update
from telegram.ext import CallbackContext

r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)

def login_page(update: Update, context: CallbackContext):
    
    user_id = update.effective_user.id
    otp = str(random.randint(100000, 999999))

    r.set(f"login_code:{otp}", user_id, ex=120) 
    
    query = update.callback_query
    query.answer()
    query.edit_message_text(f"Sizning kirish kodingiz: {otp}\nUni saytga kiriting.")
