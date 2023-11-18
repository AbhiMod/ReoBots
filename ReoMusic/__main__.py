


import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from ReoMusic import LOGGER, app, userbot
from ReoMusic.core.call import Insane
from ReoMusic.plugins import ALL_MODULES
from ReoMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("ReoMusic").error(
            "WTF Baby ! Atleast add a pyrogram string, How Cheap..."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("ReoMusic.plugins" + all_module)
    LOGGER("ReoMusic.plugins").info("Necessary Modules Imported Successfully.")
    await userbot.start()
    await Insane.start()
    try:
        await Insane.stream_call("https://telegra.ph/file/e5938d9ca8fb7c2724f80.jpg")
    except NoActiveGroupCall:
        LOGGER("ReoMusic").error(
            "[ERROR] - \n\nHey Baby, firstly open telegram and turn on voice chat in Logger Group else fu*k off. If you ever ended voice chat in log group i will stop working and users will."
        )
        sys.exit()
    except:
        pass
    await Insane.decorators()
    LOGGER("ReoMusic").info("Music Bot Started Successfully ❣️")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("ReoMusic").info("Stopping Music Bot.")
