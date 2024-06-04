
import asyncio
from typing import Optional
from random import randint
from pyrogram.types import Message, ChatPrivileges
from pyrogram import Client, filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from AnonXMusic.utils.database import *
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant, ChatAdminRequired
from AnonXMusic import app, Userbot
from typing import List, Union
from pyrogram import filters
from AnonXMusic.core.call import JARVIS
from pyrogram.types import VideoChatEnded, Message
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.exceptions import (NoActiveGroupCall, TelegramServerError, AlreadyJoinedError)

@app.on_message(filters.command(["مين في الكول"], ["", "!"]))
async def strcall(client, message):
    assistant = await group_assistant(JARVIS, message.chat.id)
    try:
        await assistant.join_group_call(message.chat.id, AudioPiped("./AnonXMusic/assets/call.mp3"), stream_type=StreamType().pulse_stream)
        text = "- الناس الموجودين ف الكول 🫶 :\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k = 0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut = "بتكلم 🗣 "
            else:
                mut = "ساكت 🔕 "
            user = await client.get_users(participant.user_id)
            k += 1
            text += f"{k} ➤ {user.mention} ➤ {mut}\n"
        text += f"\nعددهم : {len(participants)}"
        await message.reply(f"{text}")
        await asyncio.sleep(7)
        await assistant.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
        await message.reply(f"الكول مقفول اصلا")
    except TelegramServerError:
        await message.reply(f"اكتب صح مين في الكول ❌")
    except AlreadyJoinedError:
        text = "الناس الموجودين ف الكول 🫶 :\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k = 0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut = "بيتكلم 🗣"
            else:
                mut = "ساكت 🔕 "
            user = await client.get_users(participant.user_id)
            k += 1
            text += f"{k} ➤ {user.mention} ➤ {mut}\n"
        text += f"\nعددهم : {len(participants)}"
        await message.reply(f"{text}")


other_filters = filters.group  & ~filters.via_bot & ~filters.forwarded
other_filters2 = (
    filters.private  & ~filters.via_bot & ~filters.forwarded
)


def command(commands: Union[str, List[str]]):
    return filters.command(commands, "")


  ################################################
async def get_group_call(
    client: Client, message: Message, err_msg: str = ""
) -> Optional[InputGroupCall]:
    assistant = await get_assistant(message.chat.id)
    chat_peer = await assistant.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (
                await assistant.invoke(GetFullChannel(channel=chat_peer))
            ).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await assistant.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await app.send_message(f"No group ᴠᴏɪᴄᴇ ᴄʜᴀᴛ Found** {err_msg}")
    return False

@app.on_message(filters.command(["افتح الكول","افتح كول"], ["", "!"]))
async def start_group_call(c: Client, m: Message):
    chat_id = m.chat.id
    assistant = await get_assistant(chat_id)
    ass = await assistant.get_me()
    assid = ass.id
    if assistant is None:
        await app.send_message(chat_id, "خطأ في المساعد")
        return
    msg = await app.send_message(chat_id, "جاري تشغيل المكالمه..")
    try:
        peer = await assistant.resolve_peer(chat_id)
        await assistant.invoke(
            CreateGroupCall(
                peer=InputPeerChannel(
                    channel_id=peer.channel_id,
                    access_hash=peer.access_hash,
                ),
                random_id=assistant.rnd_id() // 9000000000,
            )
        )
        await msg.edit_text("تم تشغيل المكالمه.. ⚡️~!")
    except ChatAdminRequired:
      try:    
        await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
                can_manage_chat=False,
                can_delete_messages=False,
                can_manage_video_chats=True,
                can_restrict_members=False,
                can_change_info=False,
                can_invite_users=False,
                can_pin_messages=False,
                can_promote_members=False,
            ),
        )
        peer = await assistant.resolve_peer(chat_id)
        await assistant.invoke(
            CreateGroupCall(
                peer=InputPeerChannel(
                    channel_id=peer.channel_id,
                    access_hash=peer.access_hash,
                ),
                random_id=assistant.rnd_id() // 9000000000,
            )
        )
        await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
            ),
        )                              
        await msg.edit_text("تم تشغيل المكالمه بنجاح.. ⚡️~!")
      except:
         await msg.edit_text("مفيش صلاحيه يقلبي ⚡")

@app.on_message(filters.command(["اقفل الكول","قفل الكول"], ["", "!"]))
async def stop_group_call(c: Client, m: Message):
    chat_id = m.chat.id
    assistant = await get_assistant(chat_id)
    ass = await assistant.get_me()
    assid = ass.id
    if assistant is None:
        await app.send_message(chat_id, "خطأ في المساعد")
        return
    msg = await app.send_message(chat_id, "جاري اغلاق المكالمه....")
    try:
        if not (
           group_call := (
               await get_group_call(assistant, m, err_msg=", ɢʀᴏᴜᴘ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴀʟʀᴇᴀᴅʏ ᴇɴᴅᴇᴅ")
           )
        ):  
           return
        await assistant.invoke(DiscardGroupCall(call=group_call))
        await msg.edit_text("تم اغلاق المكالمه.. ⚡️~!")
    except Exception as e:
      if "GROUPCALL_FORBIDDEN" in str(e):
       try:    
         await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
                can_manage_chat=False,
                can_delete_messages=False,
                can_manage_video_chats=True,
                can_restrict_members=False,
                can_change_info=False,
                can_invite_users=False,
                can_pin_messages=False,
                can_promote_members=False,
             ),
         )
         if not (
           group_call := (
               await get_group_call(assistant, m, err_msg=", ɢʀᴏᴜᴘ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴀʟʀᴇᴀᴅʏ ᴇɴᴅᴇᴅ")
           )
         ):  
           return
         await assistant.invoke(DiscardGroupCall(call=group_call))
         await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
            ),
         )                              
         await msg.edit_text("تم اغلاق المكالمه بنجاح ⚡️~!")
       except:
         await msg.edit_text("لما تكبر هبقا اقفل المكالمه لاجلك")