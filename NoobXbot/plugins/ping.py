import time
from datetime import datetime

import psutil
from NoobXbot import Music_START_TIME, app
from NoobXbot.NoobXUtilities.helpers.time import get_readable_time
from pyrogram import filters


async def bot_sys_stats():
    bot_uptime = int(time.time() - Music_START_TIME)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    stats = f"""
𝚆𝚘𝚔𝚎 𝚄𝚙 𝚂𝚒𝚗𝚌𝚎: {get_readable_time((bot_uptime))}
𝙲𝚙𝚞: {cpu}%
𝚁𝚊𝚖: {mem}%
𝙳𝚒𝚜𝚔: {disk}%
"""
    return stats


@app.on_message(filters.command("ping"))
async def ping(_, message):
    uptime = await bot_sys_stats()
    start = datetime.now()
    response = await message.reply_text("ping...")
    end = datetime.now()
    resp = (end - start).microseconds / 1000
    await response.edit(
        f"**𝙿𝚘𝚗𝚐!**\n`🎵{resp} ms`\n\n<b><u>𝙰𝚕𝚒𝚟𝚎 𝚁𝚎𝚜𝚞𝚕𝚝𝚜:</u></b>{uptime}"
    )
