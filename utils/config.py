import os

from dotenv import load_dotenv

load_dotenv()


class Data:
    TOKEN = os.getenv("TOKEN")
    Register_url = os.getenv("Register_url")
    Login_url = os.getenv("Login_url")

settings = Data()

class RegisterStep:
    full_name, phone_number, avatar , confirm = range(4)