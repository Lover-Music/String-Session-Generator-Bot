# Channel : https//t.me/ruangzeeb

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

Saya adalah {me} 
Bot ini dapat membuat semua type Session.
Coba bot ini sekarang!!!""",
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
