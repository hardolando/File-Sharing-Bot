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
            text = "WELCOME TO A§V GROUP\nHere is the main list of A§V CHANNEL AND GROUP :\n○ MAIN CHANNEL : <a href='https://t.me/asupanviralid'>A§ID</a>\n○ RARE CONTENT : <a href='https://t.me/asupanviralid2'>A§ID2</a>\n○ UNDERAGES : <a href='https://t.me/asupanviralbovchil'>A§ID BOVCHL</a>\n\nOFFICIAL A§V GROUP :/n/n○ MAIN GROUP CHAT : <a href='https://t.me/INFOLINKASV'>GROUP</a>\n.\n○ CONTACT PERSON/INFO VVIP : <a href='https://t.me/asvservicecenter'>ADMIN A§V</a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Iya Paham", callback_data = "close")
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
