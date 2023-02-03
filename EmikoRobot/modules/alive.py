
import os

import re

from platform import python_version as kontol

from telethon import events, Button

from telegram import __version__ as x

from telethon import __version__ as y

from pyrogram import __version__ as z

from Messi.events import register

from Messi import telethn as tbot

PHOTO = "https://telegra.ph/file/f2d26142683736ab56f00.jpg"

@register(pattern=("awake mitsuri"))

async def awake(event):

  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Mitsuri AI** \n\n"

  TEXT += "🗡 **I'm Working Properly** \n\n"

  TEXT += f"🗡 **My Masters : [Hashira Techdivision](https://t.me/Hashira_techdivision)** \n\n"

  TEXT += f"🗡 **Library Version :** `{x}` \n\n"

  TEXT += f"🗡 **Telethon Version :** `{y}` \n\n"

  TEXT += f"🗡 **Pyrogram Version :** `{z}` \n\n"

  TEXT += "**💓 Thanks For Adding Me Here 💓**"

  BUTTON = [[Button.url("Help", "https://t.me/KanrojiMitsuriRobot?start=help"), Button.url("My Headquarters", "https://t.me/Hashira_Techdivision")]]

  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
