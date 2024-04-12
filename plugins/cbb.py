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
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>𓆰𝒀𝒖𝒖𝒊𝒄𝒉𝒊~𝑺𝒂𝒎𝒂𓂀</a>\n○ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href='https://telegra.ph/file/220bc38696e912c4ad81a.mp4'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n○ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/Animes_vq'>ᴀɴɪᴍᴇ ᴜɴɪᴛʏ</a>\n○ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href='https://t.me/THE_VANQUISHERS'>ᴛʜᴇ ᴠᴀɴϙᴜɪsʜᴇʀs</a>\n○ ᴀɴɪᴍᴇ ᴄʜᴀᴛ : <a href='https://t.me/weebzonex'>ᴡᴇᴇʙ ᴢᴏɴᴇ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ᴘʀᴇᴍɪᴜᴍ', url='https://t.me/OtakuFlix_Network/4639')
                    ]
                ]t
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

# ɪ ᴀᴍ ɴᴏᴛ ɪɴᴛᴇʀᴇsᴛᴇᴅ ɪɴ ʙᴇɪɴɢ ʏᴏᴜʀ sᴇᴄᴏɴᴅ ғᴀᴛʜᴇʀ ... sᴏ ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴍʏ ᴄʀᴇᴅɪᴛ...

#⋗  ᴛᴇʟᴇɢʀᴀᴍ - @Codeflix_bots

#ᴛʜɪs ʟɪɴᴇ ɪs ғᴏʀ ᴄᴏᴘʏ-ᴘᴀsᴛᴇʀs...
#...ᴡʜɪʟᴇ ʏᴏᴜ ᴀʀᴇ ʀᴇᴍᴏᴠɪɴɢ ᴍʏ ᴄʀᴇᴅɪᴛ ᴀɴᴅ ᴄᴀʟʟɪɴɢ ʏᴏᴜʀsᴇʟғ ᴀ ᴅᴇᴠᴇʟᴏᴘᴇʀʀ...
 # _____ ᴊᴜsᴛ ɪᴍᴀɢɪɴᴇ, Aᴛ ᴛʜᴀᴛ ᴛɪᴍᴇ ɪ ᴀᴍ ғᴜᴄᴋɪɴɢ ʏᴏᴜʀ ᴍᴏᴍ ᴀɴᴅ sɪs ᴀᴛ sᴀᴍᴇ ᴛɪᴍᴇ, ʜᴀʀᴅᴇʀ & ᴛᴏᴏ ʜᴀʀᴅᴇʀ...

#- ᴄʀᴇᴅɪᴛ - Github - @Codeflix-bots , @erotixe
#- ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛ..
#- ᴛʜᴀɴᴋ ʏᴏᴜ ᴄᴏᴅᴇғʟɪx ʙᴏᴛs ғᴏʀ ʜᴇʟᴘɪɴɢ ᴜs ɪɴ ᴛʜɪs ᴊᴏᴜʀɴᴇʏ 
#- ᴛʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ɢɪᴠɪɴɢ ᴍᴇ ᴄʀᴇᴅɪᴛ @Codeflix-bots  
#- ғᴏʀ ᴀɴʏ ᴇʀʀᴏʀ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ -> ᴛᴇʟᴇɢʀᴀᴍ @codeflix_bots Community @Otakflix_Network </b>
