from ReoMusic import app
from pyrogram import filters
from pyrogram.errors import MessageNotModified
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    InputMediaVideo,
    Message,
)
import config
from config import BANNED_USERS, CLEANMODE_DELETE_MINS, MUSIC_BOT_NAME, OWNER_ID


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
        InputMediaVideo("https://graph.org/file/14070f920e9294e203166.mp4"),
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data=f"settingsback_helper")]]
        ),
    )

@app.on_callback_query(filters.regex("gib_source") & ~BANNED_USERS)
@languageCB
async def gib_repo(client, callback_query, _):
    await send_source_message(callback_query)

@app.on_message(
    filters.command("repo") & filters.group & ~filters.edited & ~BANNED_USERS
)
@language
async def repo_cmds(client, message: Message, _):
    await send_source_message(message)

@app.on_message(
    filters.command("source") & filters.group & ~filters.edited & ~BANNED_USERS
)
@language
async def source_cmds(client, message: Message, _):
    await send_source_message(message)
