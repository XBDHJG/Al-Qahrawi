import asyncio
from pyrogram import Client, filters
from random import choice
from pyrogram import filters
from config import BANNED_USERS
from ANNIEMUSIC import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest

REPLY_MESSAGE = "**🧑🏻‍✈️︙اهلا بك بك عزيزي العضو ♥️**\n**⤵️︙ اليـكـ كيب الاعضاء الخاص بسورس ريل**"
REPLY_MESSAGE_BUTTONS = [
    [
             ("المبرمج"),                   
             ("سورس")

          ],
          [
              ("✨افلام"),
              ("✨اغاني") 
          ],
          [
             ("┈───┈─⦉ 𝗥𝗲𝗮𝗟 ⦊─┈───┈") 
          ],
          [
             ("✨حروف"),
             ("✨انصحني") 
          ],
          [
             ("✨ازكار"),
             ("✨زخارف") 
          ],
          [
             ("┈───┈─⦉ 𝗥𝗲𝗮𝗟 ⦊─┈───┈") 
          ],
          [
             ("✨كت"),
              ("✨صوره")
          ],
          [
              ("✨انمي"),
              ("✨حكمه")
          ],
          [
             ("┈───┈─⦉ 𝗥𝗲𝗮𝗟 ⦊─┈───┈")     
          ],
          [
             ("العاب✨"),
             ("✨مهنتي")
          ],
          [
             ("✨غنيلي"),
             ("✨متحركه")
          ],
          [
             ("┈───┈─⦉ 𝗥𝗲𝗮𝗟 ⦊─┈───┈")     
          ],
          [
             ("✨متحركه"),
             ("✨اقتباسات")
          ],
          [
             ("✨هيدرات"),
             ("✨صور بنات")
          ],
          [           
        ("❎ ¦ حذف الكيبورد")
    ]
]



@app.on_message(filters.regex("^/real"), group=39)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )
        

@app.on_message(filters.command(["❎ ¦ حذف الكيبورد"], ""))
async def upbkgt(client: Client, message: Message):
    await message.reply_text(
        text="""❎ ¦ تم حذف الكيبورد بنجاح""",
        reply_markup=ReplyKeyboardRemove()
    )
