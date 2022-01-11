from typing import List, Union 

from pyrogram import filters

other_filters=filters.group & ~filters.edited & ~filters.via_bot & ~filters.forworded
other_filters2 = (
     filters.private & ~filters.edited & ~filters.via_bot & ~filters.forworded
)


def command(commands: Union[sts, List[str]]:
    return filters.command(commands, /)
