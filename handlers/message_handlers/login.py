import random
import redis
import random

from telegram import Update
from telegram.ext import CallbackContext

r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)

def login_page(update: Update, context: CallbackContext):
    
    user_id = update.effective_user.id
    user_key = f"login_user:{user_id}"

    if r.get(user_key):
        update.message.reply_html(
            f"Eski codingiz hali amal qiladi"
        )
    else:
        r_code = str(random.randint(100000, 999999))

        r.set(user_key,r_code,ex=120)
        r.set(f"login_code:{r_code}",user_id,ex=120)

        update.message.reply_html(
        f"🔒 Code: <code>{r_code}</code>"
        )