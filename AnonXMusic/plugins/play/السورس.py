#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @WA_ADRENALEN
#𝙳𝙴𝚅 𝙰𝙳𝚁𝙴𝙽𝙰𝙻𝙴𝙽 : @DEV_ADRENALEN
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @BAR_ADRENALEN
#Omar AnonXMusic تم التعديل بواسطة 🎸 ⋅
import asyncio
from asyncio import gather
import os
import time
import requests
from pyrogram import enums
from pyrogram import types
import aiohttp
from pyrogram.types import CallbackQuery
from pyrogram import filters
from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait



##############################################################
##############################################################
          
     
@app.on_message(filters.command(["سورس","السورس","مصنع","صانع"], ""), group=221213)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/d7f84f3abf21196ccd7e5.jpg",
        caption=f"""╭── • [⌯𝐃𝐞𝐕 𝐃𝐞𝐕𝐞𝐋⌯](https://t.me/XB_DV) • ──╮\n[⌯𝐃𝐞𝐕 𝐍𝐚𝐑𝐮𝐓𝐨⌯](https://t.me/GGCQU)\n[⌯𝐒𝐨𝐔𝐫𝐂𝐞 𝐌𝐚𝐑𝐯𝐞𝐍⌯](https://t.me/SOURCE_MARVEN)\n╰── • [⌯𝐃𝐞𝐕 𝐒𝐨𝐔𝐫𝐂𝐞⌯](https://t.me/DEV_MARVEN) • ──╯""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "‹ 𝐃𝐞𝐕 𝐃𝐞𝐕𝐞𝐋 › ", url=f"https://t.me/XB_DV"),
                ],[
                    InlineKeyboardButton(
                        "‹ 𝐃𝐞𝐕 𝐍𝐚𝐑𝐮𝐓𝐨 ›", url=f"https://t.me/GGCQU"), 
                    InlineKeyboardButton(
                        "‹ 𝐒𝐨𝐔𝐫𝐂𝐞 𝐌𝐚𝐑𝐯𝐞𝐍 ›", url=f"https://t.me/SOURCE_MARVEN"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️🎸 ⋅ ›", url=f"https://t.me/DffD1bot?startgroup=True"),
            ]
        ]
         ),parse_mode=enums.ParseMode.MARKDOWN)



@app.on_message(filters.command(["مطور السورس","ناروتو"], ""), group=221212)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6d43ed90307453f7cbc6f.jpg",
        caption=f"""ғᴀᴄᴋ ʏᴏᴜ ʟᴏᴠᴇ ↻.""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        " ˖ 𝐃𝐞𝐕 𝐍𝐚𝐑𝐮𝐓𝐨 ˖ ", url=f"https://t.me/GGCQU"),
                ],[
                    InlineKeyboardButton(
                        " ˖ 𝐃𝐞𝐕 𝐂𝐡𝐚𝐧𝐞𝐞𝐋 ˖ ", url=f"https://t.me/FPPCl"), 
                    InlineKeyboardButton(
                        " ˖ 𝐁𝐨𝐓 𝐆𝐞𝐆𝐞 ˖ ", url=f"https://t.me/GI_EGYBOT"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️🎸 ⋅ ›", url=f"http://t.me/GI_EGYBOT?startgroup=new"),
            ]
        ]
         ),
     )

@app.on_message(filters.command(["مبرمج السورس","ديڤل"], ""), group=221212)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1ed441c02d9f8972b9e40.jpg",
        caption=f"""دمـاغـي زحـمـه م فـاضـي ،، مـتـجـيـش فـطـريـقـي عـشـان مسـوحـكـش""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        " ‹ 𝐃𝐞𝐕 𝐃𝐞𝐕𝐞𝐋 › ", url=f"https://t.me/XB_DV"),
                ],[
                    InlineKeyboardButton(
                        "‹ 𝐒𝐨𝐔𝐫𝐂𝐞 𝐌𝐚𝐑𝐯𝐞𝐍 ›", url=f"https://t.me/SOURCE_MARVEN"), 
                    InlineKeyboardButton(
                        "‹ 𝐁𝐨𝐓 𝐍𝐞𝐌𝐨 ›", url=f"https://t.me/DffD1bot"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️🎸 ⋅ ›", url=f"http://t.me/DffD1bot?startgroup=new"),
            ]
        ]
         ),
     )

@app.on_message(filters.command(["oooo","pppppp"], ""), group=221212)
async def huhh(client: Client, message: Message):
    await message.reply_photo( 
      photo=f"https://telegra.ph/file/81471e464fd78152dbdec.jpg",
        caption=f"""• ⌯ 𝐓𝐇𝐄.𝐒𝐎𝐔𝐑𝐂𝐄.𝐀𝐃𝐑𝐄𝐍𝐀𝐋𝐄𝐍 ⌯ •\n- سولو الـ شء 💘😂 ⋅""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        " ‹ قناة السورس 💘 ⋅ › ", url=f"https://t.me/WA_AnonXMusic"),
                ],[
                    InlineKeyboardButton(
                        "⌯ سولو الـ تونز 💘 ⋅ ⌯", url=f"https://t.me/HA_RY2"), 
                    InlineKeyboardButton(
                        "⌯ ع ــمر ادرينالين 💘 ⋅ ⌯", url=f"https://t.me/DEV_ADRENALEN"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️🎸 ⋅ ›", url=f"http://t.me/Xx_MUOSIC_BOT?startgroup=new"),
            ]
        ]
         ),
     )

@app.on_message(filters.command(["lllllll","lllllll"], ""), group=221212)
async def huhh(client: Client, message: Message):
    await message.reply_photo( 
      photo=f"https://telegra.ph/file/1d76ff4496515c122c251.jpg",
        caption=f"""• ⌯ 𝐓𝐇𝐄.𝐒𝐎𝐔𝐑𝐂𝐄.𝐀𝐃𝐑𝐄𝐍𝐀𝐋𝐄𝐍 ⌯ •\n- فرعون الـ شء 💘😂 ⋅""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        " ‹ قناة السورس 💘 ⋅ › ", url=f"https://t.me/WA_AnonXMusic"),
                ],[
                    InlineKeyboardButton(
                        "⌯ فـرعون الـ تونز 💘 ⋅ ⌯", url=f"https://t.me/DEV_FAR3ON"), 
                    InlineKeyboardButton(
                        "⌯ ع ــمر ادرينالين 💘 ⋅ ⌯", url=f"https://t.me/DEV_ADRENALEN"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️🎸 ⋅ ›", url=f"http://t.me/Xx_MUOSIC_BOT?startgroup=new"),
            ]
        ]
         ),
     )
     


    
@app.on_message(filters.command(["kkkkkk","kkkkkk"], ""), group=221212)
async def huhh(client: Client, message: Message):
    await message.reply_photo( 
      photo=f"https://telegra.ph/file/783c1ff05a1480c023f9e.jpg",
        caption=f"""• ⌯ 𝐓𝐇𝐄.𝐒𝐎𝐔𝐑𝐂𝐄.𝐀𝐃𝐑𝐄𝐍𝐀𝐋𝐄𝐍 ⌯ •\n- فيرس الـ شء 💘😂 ⋅""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        " ‹ قناة السورس 💘 ⋅ › ", url=f"https://t.me/WA_AnonXMusic"),
                ],[
                    InlineKeyboardButton(
                        "⌯ فيرس الـ تونز 💘 ⋅ ⌯", url=f"https://t.me/Xx_VAiRS_xX"), 
                    InlineKeyboardButton(
                        "⌯ ع ــمر ادرينالين 💘 ⋅ ⌯", url=f"https://t.me/DEV_ADRENALEN"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️🎸 ⋅ ›", url=f"http://t.me/Xx_MUOSIC_BOT?startgroup=new"),
            ]
        ]
         ),
     )

@app.on_message(filters.command(["اسمي","اسمي اي","قول اسمي"], ""), group=123222)
async def vgdg(client: Client, message: Message):
    await message.reply_text(
        f"""- اسمك » ⦗ {message.from_user.mention} ⦘ 💘 ⋅""") 


##############################################################
##############################################################
##############################################################
  


#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @WA_ADRENALEN
#𝙳𝙴𝚅 𝙰𝙳𝚁𝙴𝙽𝙰𝙻𝙴𝙽 : @DEV_ADRENALEN
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @BAR_ADRENALEN
#Omar AnonXMusic تم التعديل بواسطة 🎸 ⋅    
