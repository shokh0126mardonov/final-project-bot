import os

from dotenv import load_dotenv

load_dotenv()


class Data:
    TOKEN = os.getenv("TOKEN")


settings = Data()