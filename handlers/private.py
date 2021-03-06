import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from pyrogram.raw.base import Update
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
from pyrogram import filters

@Client.on_message(command("start") & filters.private )
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c247284e8ddc50f01a314.png",
        caption=f"""**๐๐ก๐ข๐ฌ ๐๐ฌ ๐๐๐ฏ๐๐ง๐๐ ๐ฅ๐๐๐ฅ๐๐ ๐ซ๐๐ฆ ๐๐ฎ๐ฌ๐ข๐ ๐๐จ๐ญ ๐๐ฎ๐ง ๐๐ง ๐๐ซ๐ข๐ฏ๐๐ญ๐ ๐ฅ ๐๐ฉ๐ฌ ๐ซ๐๐๐ซ๐ฏ๐๐ซ ๐ ๐๐๐๐ฅ โค๏ธ ๐๐ข๐ ๐ก ๐๐ฎ๐๐ฅ๐ข๐ญ๐ฒ ๐๐ฎ๐ฌ๐ข๐ ๐ง ๐๐ง ๐๐**""",
    reply_markup=InlineKeyboardMarkup(
            [   
                [
                    InlineKeyboardButton("โ แดกแดษดษดแด แดแดแด แดแด สแดสสโ โ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
               ],
                [
                    InlineKeyboardButton(
                        "โฅ๏ธ Creator โฅ๏ธ", url=f"https://t.me/Murat_30_God")
               ],
                [
                    InlineKeyboardButton(
                        "Repo โจ", url=f"https://github.com/kaal0408/Music")
               ], 
                [
                    InlineKeyboardButton(
                        "๐จโ๐ป YouTube", url=f"https://youtube.com/channel/UCpZBwvZJdRsInUBgAWfpVMA")
               ],
                [
                    InlineKeyboardButton(
                        "๐ Commands ๐", callback_data=f"cbcmds")
                ]
                
           ]
       ),
    )

@Client.on_message(command(["repo"]) & filters.group )
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c247284e8ddc50f01a314.png",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฅ Repo ๐", url=f"https://github.com/kaal0408/Music")
                ]
            ]
        ),
    )


@bot.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.answer("Commands Menu")
    await query.edit_message_text(
        f"""**ยป แดแดษชษด แดแดแดแดแดษดแด๊ฑ ยซ**
ยป /play (Song Name/Link) - Play Music
ยป /pause - Pause The Song
ยป /resume - Resume The Song
ยป /skip - switch to next Song
ยป /end - Stop The Streaming
ยป /join or /userbotjoin - Invite Assistant To Your Group
ยป /mute - Mute The Assistant On Voice Chat
ยป /unmute - UnMute The Assistant On Voice Chat
ยป /playlist - Show You The Playlist
ยป /broadcast  - To broadcast a message (sudo)
ยป /gcast  - To broadcast a message (sudo)
ยป /restart - Restart The Bot
๐ฅต __๐๐ฐ๐ธ๐ฆ๐ณ๐ฆ๐ฅ ๐๐บ Manjeet__ ๐ฅต""")
