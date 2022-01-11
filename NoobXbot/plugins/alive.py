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
    parts = []
    for unit, div in TIME_DURATION_UNITES:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0
            parts.append('{} {}{})'
                        .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

@Client.on_message(filters.command(["alive", f"alive@{BOT_USERNAME}"]))
async def alive(client, message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_second()
    uptime = await _human_time_duration(int(uptime_sec))
    await client.send_photo(message.chat.id,
        photo=f"(https://telegra.ph/file/0b60fa847086549786219.jpg)
        captin=f""" Master {message.from_user.mention()}, I'm NoobXRobot.**
      **I'm working perfectly**
      **Bot : 0.7 Jan Update**
      **My Master : [{OWNER_USERNAME}](https://t.me/userderdead})**
      **Service Time : `{uptime}`
      **Thanks For Using Me Dude 🎵**"",
