##Config

from os import getenv

from dotenv import load_dotenv
from pyrogram import Client
from pytgcalls import PyTgCalls

load_dotenv()
SESSION_NAME = getenv('SESSION_NAME', 'session')
SESSION_NAME2 = getenv('SESSION_NAME2', 'session')
BOT_TOKEN = getenv('BOT_TOKEN')
API_ID = int(getenv('API_ID', "13474125"))
API_HASH = getenv('API_HASH')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '30'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ . , : ; !').split())
MONGO_DB_URI = getenv("MONGO_DB_URI")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001715140522'))
ASS_ID = int(getenv("ASS_ID", '2144966937'))
OWNER_ID = list(map(int, getenv('OWNER_ID', '').split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", None)
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", None)
ASS_ACC = Client(
    SESSION_NAME2,
    API_ID,
    API_HASH,
)
call_py = PyTgCalls(ASS_ACC)
