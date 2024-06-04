from pyrogram import filters
from pyrogram.types import Message
from AnonXMusic.mongo.pretenderdb import impo_off, impo_on, check_pretender, add_userdata, get_userdata, usr_data
from AnonXMusic import app




@app.on_message(filters.group & ~filters.bot & ~filters.via_bot, group=69)
async def chk_usr(_, message: Message):
    if message.sender_chat or not await check_pretender(message.chat.id):
        return
    if not await usr_data(message.from_user.id):
        return await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    usernamebefore, first_name, lastname_before = await get_userdata(message.from_user.id)
    msg = ""
    if (
        usernamebefore != message.from_user.username
        or first_name != message.from_user.first_name
        or lastname_before != message.from_user.last_name
    ):
        msg += f"""
**🔓 مسكته الشقي 🔓**
➖➖➖➖➖➖➖➖➖➖➖➖
**🍊 اسمه** : {message.from_user.mention}
**🍅 الايدي بتاعه** : {message.from_user.id}
➖➖➖➖➖➖➖➖➖➖➖➖\n
"""
    if usernamebefore != message.from_user.username:
        usernamebefore = f"@{usernamebefore}" if usernamebefore else "NO USERNAME"
        usernameafter = (
            f"@{message.from_user.username}"
            if message.from_user.username
            else "NO USERNAME"
        )
        msg += """
**🐻‍❄️ غير يوزره 🐻‍❄️**
➖➖➖➖➖➖➖➖➖➖➖➖
**🎭 من** : {bef}
**🍜 ل** : {aft}
➖➖➖➖➖➖➖➖➖➖➖➖\n
""".format(bef=usernamebefore, aft=usernameafter)
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if first_name != message.from_user.first_name:
        msg += """
**🪧 غير الاسم الاول 🪧**
➖➖➖➖➖➖➖➖➖➖➖➖
**🔐 من** : {bef}
**🍓 ل** : {aft}
➖➖➖➖➖➖➖➖➖➖➖➖\n
""".format(
            bef=first_name, aft=message.from_user.first_name
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if lastname_before != message.from_user.last_name:
        lastname_before = lastname_before or "NO LAST NAME"
        lastname_after = message.from_user.last_name or "NO LAST NAME"
        msg += """
**🪧 غير الاسم الثاني 🪧**
➖➖➖➖➖➖➖➖➖➖➖➖
**🚏من** : {bef}
**🍕 ل** : {aft}
➖➖➖➖➖➖➖➖➖➖➖➖\n
""".format(
            bef=lastname_before, aft=lastname_after
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if msg != "":
        await message.reply_photo("https://te.legra.ph/file/70872d57cab08aa096a04.jpg", caption=msg)


@app.on_message(filters.command(["تنبيه الحساب"], "") & ~filters.bot & ~filters.via_bot)
async def set_mataa(_, message: Message):
    if len(message.command) == 1:
        return await message.reply("**اكتب الامر كده تنبيه الحساب تفعيل**")
    if message.command[1] == "تفعيل":
        cekset = await impo_on(message.chat.id)
        if cekset:
            await message.reply("**تنبيه الحساب شغال بالفعل**")
        else:
            await impo_on(message.chat.id)
            await message.reply(f"**تم تفعيل تنبيه الحساب بنجاح** {message.chat.title}")
    elif message.command[1] == "تعطيل":
        cekset = await impo_off(message.chat.id)
        if not cekset:
            await message.reply("**تنبيه الحساب معطل بالفعل**")
        else:
            await impo_off(message.chat.id)
            await message.reply(f"**تم تعطيل تنبيه الحساب بنجاح** {message.chat.title}")
    else:
        await message.reply("**اكتب الامر كده تنبيه الحساب تفعيل**")
