import os

from dotenv import load_dotenv

load_dotenv()


class Data:
    TOKEN = os.getenv("TOKEN")

settings = Data()


class RegisterStep:
    full_name, phone_number, avatar , confirm = range(4)