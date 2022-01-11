from os import path
from pyrogram import Client, filters
from pyrogram.types import Message
from time import time 
from datetime import datetime 
from NoobXbot.config import (
    BOT_USERNAME,
    GROUP_SUPPORT,
)
from NoobXbot.helpers.filters import command, other_filters
from pyrogram.types import Message, InlineKeyBoardMarkup, InlinekeyboadrdButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITES = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
