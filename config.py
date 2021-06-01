import os

class Configs(object):

TOKENN = os.environ.get("TOKENNN", "")
USERNAMEE = os.environ.get("USERNAMEEE", "")
BOT_CHAT_IDD = int(os.environ.get("CHATTT", ""))


class Config(object):

TOKEN=Configs.TOKENN
USERNAME=Configs.USERNAMEE
BOT_CHAT_ID=Configs.BOT_CHAT_IDD
