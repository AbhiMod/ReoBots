from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaVideo,
    Message,
)
from ReoMusic import app  # Assuming ReoMusic is the name of your Pyrogram client
import config
from config import BANNED_USERS

@app.on_message(filters.command("id"))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"**ʏᴏᴜʀ ɪᴅ**: `{message.from_user.id}`\n**{reply.from_user.first_name}'s ɪᴅ**: `{reply.from_user.id}`\n**ᴄʜᴀᴛ ɪᴅ**: `{message.chat.id}`"
        )
    else:
        message.reply(
            f"**ʏᴏᴜʀ ɪᴅ**: `{message.from_user.id}`\n**ᴄʜᴀᴛ ɪᴅ**: `{message.chat.id}`"
        )


async def send_source_message(callback_query):
    await callback_query.edit_message_media(
        media=InputMediaVideo("https://graph.org/file/14070f920e9294e203166.mp4"),
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data=f"settingsback_helper")]]
        ),
    )

@app.on_callback_query(filters.regex("gib_source") & ~BANNED_USERS)
async def gib_repo(_, callback_query: CallbackQuery):
    await send_source_message(callback_query)

@app.on_message(
    filters.command("repo") & filters.group & ~filters.edited & ~BANNED_USERS
)
async def repo_cmds(_, message: Message):
    # Since message does not have edit_message_media method, you can't use it here
    # Instead, you can send a new message or use other appropriate methods
    await send_source_message(message)

@app.on_message(
    filters.command("source") & filters.group & ~filters.edited & ~BANNED_USERS
)
async def source_cmds(_, message: Message):
    # Same as above, if you want to edit the original message, you can't use edit_message_media
    await send_source_message(message)
