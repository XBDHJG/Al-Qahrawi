import asyncio
from AnonXMusic import app
from pyrogram import filters
from pyrogram.types import ChatJoinRequest
from pyrogram.errors import FloodWait


@app.on_chat_join_request(filters.group | filters.channel)
async def approve(_, m: ChatJoinRequest):
    if not m.from_user:
        return
    try:
        await app.approve_chat_join_request(m.chat.id, m.from_user.id)
    except FloodWait as e:
        logging.info(f"Sleeping for {e.x + 2} seconds due to floodwaits!")
        await asyncio.sleep(e.x + 2)
        await app.approve_chat_join_request(m.chat.id, m.from_user.id)
