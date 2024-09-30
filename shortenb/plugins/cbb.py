#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>◈ ʙᴏᴛ ᴏᴡɴᴇʀ: <a>ʟᴜꜰꜰʏ</a>\n◈ ᴄʀᴇᴀᴛᴏʀ: <a>Sᴀᴍ</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/+g7GOrD2ZK6UyZmEx>AᴜᴅɪᴏVᴇʀsᴇ Nᴇᴛᴡᴏʀᴋ</a>\n◈ Mᴀɪɴ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/+PH9yiLVn_HMyNzJl>Pᴏᴄᴋᴇᴛ Fᴍ Eɴɢʟɪsʜ </a>\n◈ Oɴɢᴏɪɴɢ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/+uLRmxKGyff9mNDQ1>Pᴏᴄᴋᴇᴛ Fᴍ Dᴀɪʟʏ</a>\n◈ Sᴜᴘᴘᴏʀᴛ Bᴏᴛ : <a href=https://t.me/PFM_SUPPORT_BOT>Sᴜᴘᴘᴏʀᴛ Bᴏᴛ</a>\n◈ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ : <a href=https://t.me/+emDyFn-ROq0wZTdl>𝖨𝗌𝗌𝗎𝖾𝗌 & 𝖴𝗉𝖽𝖺𝗍𝖾 - ᴘꜰᴍ</a>\n </b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 Sᴜᴘᴘᴏʀᴛ Bᴏᴛ', url='https://t.me/PFM_SUPPORT_BOT')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
