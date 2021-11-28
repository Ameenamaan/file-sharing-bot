#(©)Codexbotz
#(©)Cold_Onez

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Mᴀsᴛᴇʀ : <a href='https://t.me/Ameen_Ameen_12'>ᵐʳ𝐔𝐧𝐤𝐧𝐨𝐰𝐧🇮🇳༒</a>\n○ Lᴀɴɢᴜᴀɢᴇ : <code>Python3</code>\n○ Lɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href='https://github.com/Ameenamaan/file-sharing-bot'>Click Here</a>\n○ Cʜᴀɴɴᴇʟ : @HDmovieDp\n○ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ : @HDmoviePp</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Cʟᴏsᴇ", callback_data = "close")
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
