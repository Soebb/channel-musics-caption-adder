import os

class Config(object):
TOKEN = os.environ.get("TOKEN", "")
USERNAME = os.environ.get("USERNAME", "")
BOT_CHAT_ID = int(os.environ.get("CHAT", ""))

