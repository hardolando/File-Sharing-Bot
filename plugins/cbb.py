#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "GW":
        await query.message.edit_text(
            text = f"Channel : @asupanviralid\n Support Group : @infolinkasv</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("dahlah", callback_data = "dah")
                    ]
                ]
            )
        )
    elif data == "dah":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
