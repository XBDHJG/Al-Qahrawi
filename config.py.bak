import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables from .env file
load_dotenv()

# Telegram API credentials - Get these from the Telegram API website
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

# Specify where to get the following credentials
OWNER_USERNAME = getenv("OWNER_USERNAME", "L_HLN")
BOT_USERNAME = getenv("BOT_USERNAME", "Zei_nbot")
BOT_NAME = getenv("BOT_NAME", "𝖗𝖊𝖆𝖑 ✘ 𝖒𝖚𝖘𝖎𝖈˼ ♪")
ASSUSERNAME = getenv("ASSUSERNAME", "GGCQO")
EVALOP = list(map(int, getenv("EVALOP", "6300938349").split()))
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
LOGGER_ID = int(getenv("LOGGER_ID", -1002014167331))
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# External APIs - Get these from their respective providers
GPT_API = getenv("GPT_API")
PLAYHT_API = getenv("PLAYHT_API")
OWNER_ID = int(getenv("OWNER_ID", 6300938349))

# Heroku deployment settings - Refer to Heroku documentation on how to obtain these
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/zxzzzx/zee")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Support and contact information - Provide your own support channels
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/CBSOURCE")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/CBSupportX")

# Server limits and configurations - These can be set based on your server configurations
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "2500"))
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

# External service credentials - Obtain these from Spotify
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")

# Telegram file size limits - Set these according to your requirements
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

# Pyrogram session strings - You need to generate these yourself
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# Bot introduction messages - These can be customized as per your preference
AMBOT = [
    "💞", "🦋", "🔍", "🧪", "🦋", "⚡️", "🔥", "🦋", "🎩", "🌈", "🍷", "🥂", "🦋", "🥃", "🥤", "🕊️",
    "🦋", "🦋", "🕊️", "🦋", "🕊️", "🦋", "🦋", "🦋", "🪄", "💌", "🦋", "🦋", "🧨"
]

AMOP = [
    "┈─┈─┈ ┈─⦉ 𝗥𝗲𝗮𝗟 ⦊─┈ ┈─┈─┈\n❖ انـا بـوت اسـمـي ( {1} ) •\n❖ استطيع تشغيل اغاني فالمكالمات •\n❖ وتشـغـيل فديو فالمكالمات •\n❖ وحـمـايـة الـجـروب من التصفية •\n❖ ويوجد اوامر تسلية والعاب ڪثيرة •\n❖ اضغط ( /real ) لعرض كيب العضو •\n❖ لـعـرض الاوامر اضـغـط فالاسفل  •\n┈─┈─┈ ┈─⦉ 𝗥𝗲𝗮𝗟 ⦊─┈ ┈─┈─┈"
]

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/d614c73c61ae132773756.png"
)
PING_VID_URL = getenv(
    "PING_VID_URL", "https://telegra.ph/file/4be43ed2aa6872337e9a8.mp4"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/917d33a663247038ddb64.jpg"
STATS_IMG_URL = "https://telegra.ph/file/9f3613d95078ff5f81120.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/917d33a663247038ddb64.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/c8db17e1612487be13571.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/6a81d918bd5d44c646205.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/917d33a663247038ddb64.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/917d33a663247038ddb64.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/06679f04da4b2fbbb12d0.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/06679f04da4b2fbbb12d0.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/06679f04da4b2fbbb12d0.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
)
