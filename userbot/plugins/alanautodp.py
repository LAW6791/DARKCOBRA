"""
Time In Profile Pic.....
Command: `.alandp`

⚠️DISCLAIMER⚠️

USING THIS PLUGIN CAN RESULT IN ACCOUNT BAN + CAS BAN + SPAM BAN + ACCOUNT SUSPENSION . WE DONT CARE ABOUT BAN, SO WE ARR USING THIS.
"""
import os
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import admin_cmd
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
from uniborg.util import admin_cmd
import asyncio
import shutil 
from userbot import ALIVE_NAME, CMD_HELP
import random, re

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

FONT_FILE_TO_USE = "userbot/helpers/styles/digital.ttf"

#Add telegraph media links of profile pics that are to be used
TELEGRAPH_MEDIA_LINKS = ["https://telegra.ph/file/b2cea1712ebaca603e6f4.jpg",
                        ]
@borg.on(admin_cmd(pattern="alandp ?(.*)"))
async def autopic(event):
    while True:
        piclink = random.randint(0, len(TELEGRAPH_MEDIA_LINKS) - 1)
        AUTOPP = TELEGRAPH_MEDIA_LINKS[piclink]
        downloaded_file_name = "./userbot/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            place_holder = None   
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        current_time = datetime.now().strftime(" {DEFAULTUSER} \n\n  %H:%M:%S \n %d/%m/%y")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 35)
        drawn_text.text((10,40), current_time, font=fnt, fill=(255,0,0))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(functions.photos.DeletePhotosRequest(await event.client.get_profile_photos("me", limit=1)))
            await event.client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo)
            
            await asyncio.sleep(90)
        except:
            return
