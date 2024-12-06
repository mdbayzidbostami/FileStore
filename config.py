#(©)t.me/CodeFlix_Bots




import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "25751497"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "c18db31105b92bba3cfa1ab685c4787f")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002126389045"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "xerox_bayzid")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5548923721"))
#Port
PORT = os.environ.get("PORT", "8030")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://bayzidpremium:bayzidpremium@cluster0.dm24s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002172515270')) #Log channel id ( make sure bot is admin )

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001960183584"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002333397554"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYnC0c7Mayqdusbi61p9V2WYcyX1Bur2ppChB_zi0APtkrKMwKH24msrXz&s=10")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYnC0c7Mayqdusbi61p9V2WYcyX1Bur2ppChB_zi0APtkrKMwKH24msrXz&s=10")

HELP_TXT = "<b>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @otakuflix_network\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/cosmic_freak>sᴜʙᴀʀᴜ</a></b>"
ABOUT_TXT = "<b>◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/cosmic_freak>subaru</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/otakuflix_network>ᴏᴛᴀᴋᴜғʟɪx ɴᴇᴛᴡᴏʀᴋ</a>\n◈ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/anime_cruise_netflix>ᴀɴɪᴍᴇ ᴄʀᴜɪsᴇ</a>\n◈ sᴇʀɪᴇs ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/webseries_flix>ᴡᴇʙsᴇʀɪᴇs ғʟɪx</a>\n◈ ᴀᴅᴜʟᴛ ᴍᴀɴʜᴡᴀ : <a href=https://t.me/pornhwaocean>ᴘᴏʀɴʜᴡᴀs</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/cosmic_freak>subaru</a></b>"
START_MSG = os.environ.get("START_MESSAGE", "<b>- ʜɪ ɪ'ᴍ ᴀ ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ-!!\n\n- ʏᴏᴜ ᴄᴀɴ sᴛᴏʀᴇ ᴀɴʏ ᴛʏᴘᴇs ᴏғ ғɪʟᴇs &amp; ᴅᴏᴄᴜᴍᴇɴᴛs ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ-!!📮\n\n- ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴍʏ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ / ɢʀᴏᴜᴘ ᴛᴏ ᴀᴄᴄᴇss ᴛʜᴇ ʙᴏᴛ-!!🪦</b>")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "5115691197 6273945163 6103092779 5231212075").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>- ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴊᴏɪɴ ᴍʏ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ &amp; ɢʀᴏᴜᴘ-!!💫\n\n- ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴍʏ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ / ɢʀᴏᴜᴘ &amp; ᴄʟɪᴄᴋ ᴏɴ ᴛʀʏ ᴀɢᴀɪɴ ʙᴜᴛᴛᴏɴ -!!🪦</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>- ғɪʟᴇ ᴜᴘʟᴏᴀᴅᴇᴅ ʙʏ : </b><b>@suryag10_yt</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>- ʙᴏᴛ ʀᴜɴɴɪɴɢ ᴛɪᴍᴇ :</b> <code>{uptime}</code>"
USER_REPLY_TEXT = "<b>- ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴘᴇʀᴍɪᴛᴛᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ-!!☹️\n\n- ᴘʟᴇᴀsᴇ ᴄᴏɴᴛʀᴀᴄᴛ @xᴇʀᴏx_ʙᴀʏᴢɪᴅ ɪ'ᴅ &amp; ɢᴇᴛ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ᴀᴄᴄᴇss ᴛʜᴇ ʙᴏᴛ-!!🪦</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
