import asyncio
from pyrogram import Client, filters
from random import choice
from pyrogram import filters
from config import BANNED_USERS
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest

REPLY_MESSAGE = "**🧑🏻‍✈️︙اهلا بك بك عزيزي العضو ♥️**\n**⤵️︙ اليـكـ كيب الاعضاء الخاص بسورس مارڤين**"
REPLY_MESSAGE_BUTTONS = [
    [
             ("مبرمج السورس"),                   
             ("مطور السورس")

          ],
          [
              ("✨افلام"),
              ("✨اغاني") 
          ],
          [
             ("┈─⦉ 𝐒𝐨𝐔𝐫𝐂𝐞 𝐌𝐚𝐑𝐯𝐄𝐧 ⦊─┈") 
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
             ("┈─⦉ 𝐒𝐨𝐔𝐫𝐂𝐞 𝐌𝐚𝐑𝐯𝐄𝐧 ⦊──┈") 
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
             ("┈─⦉ 𝐒𝐨𝐔𝐫𝐂𝐞 𝐌𝐚𝐑𝐯𝐄𝐧 ⦊─┈")     
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
             ("┈─⦉ 𝐒𝐨𝐔𝐫𝐂𝐞 𝐌𝐚𝐑𝐯𝐄𝐧 ⦊──┈")     
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
