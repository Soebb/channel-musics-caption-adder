import os

class Config(object):

TOKEN = "1821784179:AAHQWfHb9X5s-F6QM5A3FbwRHOgl4DgVkFM"
USERNAME = os.environ.get("USERNAME", "")
BOT_CHAT_ID = int(os.environ.get("CHAT", ""))
