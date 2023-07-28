#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config(21335027, default=None, cast=int)
API_HASH = config("76926c6bdbf143ab8fc9679be988f822", default=None)
BOT_TOKEN = config("6092747783:AAFgtXVww1Gs30LsWNSxEZ95-KlAw-Rgfa4", default=None)
SESSION = config("BQFFi_MAoM0vZ0d-XyRVHCLbqltZGAPUYsO7Zk6v5pgotUoU3RkIpvGnyFgIpMUcJ7AK_wluYyALLZKx8586s1Qszq5xsreXY8Squ_yYaFs0TyTP1LL9WT1ci4iRJFYbQcwtFF4Clfvfnd93NftcGPqJjABa8mRkUCq11fVToEz_j7ucBhBmKe3URAHsXTvbgCUkkUMsQPGSB0qvpuM9yAGQtlYJj7PH50SE6WHyzSXrVvkO9p_C-VKXvh2uawQRs-zmmBGkooHLrGwmHe6dhmZhjIiTRFVcKZZtgEIZ6ul2TmWadijrrRGLLIhkIZHG397Z-IKi9esCsyEPZNEkJ2aEbJCywAAAAAA6ZWADAA", default=None)
FORCESUB = config("Cx653A", default=None)
AUTH = config(979722243, default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
