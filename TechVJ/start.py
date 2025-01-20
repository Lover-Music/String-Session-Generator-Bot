from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID
from TechVJ.db import db

# Renaming the filter function to avoid conflict with built-in names
def command_filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(command_filter("start"))
async def start(bot: Client, msg: Message):
    me = (await bot.get_me()).mention  # Changed variable name to avoid shadowing built-in function name 'me'
    await msg.reply_text(
        text=f"""Hello {msg.from_user.mention} 💫,

Welcome {me} 
If you don't trust this bot, 
Please stop reading this message
Delete this chat

Still reading?
You can use me to generate Pyrogram and Telethon string session. Use below buttons to learn more !

By [Lover Team]({link})!!!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="💥Generate Session💥", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("💥Support💥", url="https://t.me/LOVER_MUSIC_SUPPORT_GROUP"),
                    InlineKeyboardButton("💥Update💥", url="https://t.me/LOVER_MUSIC_SUPPORT")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
