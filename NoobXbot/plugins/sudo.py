import os

from NoobXbot import OWNER, app
from NoobXbot.NoobXUtilities.database.sudo import add_sudo, get_sudoers, remove_sudo
from pyrogram import filters
from pyrogram.types import Message


@app.on_message(filters.command("addsudo") & filters.user(OWNER))
async def useradd(_, message: Message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            await message.reply_text(
                "Reply to user messages or provide username/username_id."
            )
            return
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        message.from_user
        sudoers = await get_sudoers()
        if user.id in sudoers:
            return await message.reply_text("Already a sudo User.")
        added = await add_sudo(user.id)
        if added:
            await message.reply_text(
                f"Added **{user.mention}** As a NoobX sudo User"
            )
            return os.execvp("python3", ["python3", "-m", "Music"])
        await edit_or_reply(message, text="An error occurred, check the logs.")
        return
    message.from_user.id
    user_id = message.reply_to_message.from_user.id
    mention = message.reply_to_message.from_user.mention
    sudoers = await get_sudoers()
    if user_id in sudoers:
        return await message.reply_text("Already a sudo User.")
    added = await add_sudo(user_id)
    if added:
        await message.reply_text(f"Added **{mention}** As a sudo User")
        return os.execvp("python3", ["python3", "-m", "Music"])
    await edit_or_reply(message, text="An error occurred, check the logs.")
    return


@app.on_message(filters.command("delsudo") & filters.user(OWNER))
async def userdel(_, message: Message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            await message.reply_text(
                "Reply to user messages or provide username/user_id."
            )
            return
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        message.from_user
        if user.id not in await get_sudoers():
            return await message.reply_text(f"Not a part of NoobX's Sudo.")
        removed = await remove_sudo(user.id)
        if removed:
            await message.reply_text(f"Delete **{user.mention}** from Sudo.")
            return os.execvp("python3", ["python3", "-m", "Music"])
        await message.reply_text(f"Sudo Deleted By NoobX Official")
        return
    message.from_user.id
    user_id = message.reply_to_message.from_user.id
    mention = message.reply_to_message.from_user.mention
    if user_id not in await get_sudoers():
        return await message.reply_text(f"Not part of Sudo Music.")
    removed = await remove_sudo(user_id)
    if removed:
        await message.reply_text(f"Delete **{mention}** from Sudo.")
        return os.execvp("python3", ["python3", "-m", "Music"])
    await message.reply_text(f"Something wrong happened.")


@app.on_message(filters.command("sudolist"))
async def sudoers_list(_, message: Message):
    sudoers = await get_sudoers()
    text = "**Sudo User List**\n\n"
    for count, user_id in enumerate(sudoers, 1):
        try:
            user = await app.get_users(user_id)
            user = user.first_name if not user.mention else user.mention
        except Exception:
            continue
        text += f"• {user}\n"
    if not text:
        await message.reply_text("No Sudo User")
    else:
        await message.reply_text(text)
