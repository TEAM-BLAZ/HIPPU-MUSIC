from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from handlers import __version__
from helpers.decorators import sudo_users_only
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_private(client: Client, message: Message):
    await message.reply_text(
        f"""<b>**☞ ✰ᗯᴇʟᴄᴏᴍᴇ {message.from_user.first_name}** \n
**☞ ✰I'ᴍ ᑭʟᴀʏ ᗰᴜsɪᴄ Oɴ Tᴇʟᴇɢʀᴀᴍ ᐯᴏɪᴄᴇ ᑕʜᴀᴛ..** \n
**☞ 📢 𝗣𝗢𝗪𝗘𝗥𝗘𝗗 𝗕𝗬 :- [ᗷʟᴀᴢᴇ](https://t.me/THE_BLAZE_NETWORK)** \n
**☞ ✰ᖴᴏʀ ᗰᴏʀᴇ ᕼᴇʟᴘ ᑌsᴇ ᗷᴜᴛᴛᴏɴs ᗷᴇʟᴏᴡ ᗩɴᴅ ᗩʙᴏᴜᴛ ᗩʟʟ ᖴᴇᴀᴛᴜʀᴇ Oғ Tʜɪs ᗷᴏᴛ, ᒍᴜsᴛ Tʏᴘᴇ /help ** 
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        " ➕ ᗩᴅᴅ ᗰᴇ Tᴏ Yᴏᴜʀ ᘜʀᴏᴜᴘ ➕ ", url=f"https://t.me/BLAZEMUSIC_BOT?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "•☞ ᕼᴏᴡ Tᴏ ᑌsᴇ ᗰᴇ 🎧", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         " •☞ ᑕᴍᴅs 🕹 ", url=f"https://telegra.ph/%E1%97%B7%CA%9F%E1%B4%80%E1%B4%A2%E1%B4%87-%E1%97%B0%E1%B4%9Cs%C9%AA%E1%B4%84-%E1%97%B7%E1%B4%8F%E1%B4%9B-09-14-2"),
                
                    InlineKeyboardButton(
                        " •☞ Oᴡɴᴇʀ 🕵 ", url=f"https://t.me/BLAZE_OWNER")
                ],[
                    InlineKeyboardButton(
                        " •☞ Տᴜᴘᴘᴏʀᴛ ᘜʀᴏᴜᴘ 📣 ", url=f"https://t.me/Blaze_Support"),
                
                    InlineKeyboardButton(
                        " •☞ Oғғɪᴄɪᴀʟ ᑕʜᴀɴɴᴇʟ 📢 ", url=f"https://t.me/THE_BLAZE_NETWORK")
                ],[
                    InlineKeyboardButton(
                        " •☞ Տᴘᴀᴍ ᘜʀᴏᴜᴘ 📡 ", url="https://t.me/BLAZE_SPAMMER")
                ],
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def start_group(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("✨ Group", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "📣 Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**Hello {message.from_user.mention()}, i'm {BOT_NAME}**\n\n✨ Bot is working normally\n🍀 My Master: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n✨ Bot Version: `v{__version__}`\n🍀 Pyrogram Version: `{pyrover}`\n✨ Python Version: `{__python_version__}`\n🍀 Uptime Status: `{uptime}`\n\n**Thanks for Adding me here, for playing music on your Group voice chat** ❤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(
    command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **Hello** {message.from_user.mention()} !

» **press the button below to read the explanation and see the list of available commands !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="❓ Basic Guide", callback_data="cbguide")]]
        ),
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
