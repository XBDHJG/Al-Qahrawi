
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from AnonXMusic import app

#--------------------------

MUST_JOIN = "SOURCE_MARVEN"
#------------------------
@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await app.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://telegra.ph/file/d7f84f3abf21196ccd7e5.jpg", caption=f" ┈─┈ ┈─⦉ 𝐒𝐨𝐔𝐫𝐂𝐞 𝐌𝐚𝐑𝐯𝐄𝐧 ⦊─┈ ┈─┈\n❖ اشـتـرڪك فـقـنـاه الـبـوت  ↯\n❖ فـي الـزر بـالاسـفـل  ↯\n❖ تم اضـغـط (  /start  ) للبدأ ↯\n  ┈───┈ ┈───┈ ┈───┈ ",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("𝐒𝐨𝐔𝐫𝐂𝐞 𝐌𝐚𝐑𝐯𝐄𝐧", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"๏ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴍᴜsᴛ_Jᴏɪɴ ᴄʜᴀᴛ ๏: {MUST_JOIN} !")
