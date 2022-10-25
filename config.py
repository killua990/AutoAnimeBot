from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "9539951"))
API_HASH = getenv("API_HASH", "89ce95095d48f7f8eb1aee490a944863")
BOT_TOKEN = getenv("BOT_TOKEN", "5419760162:AAElD9p1f05hUIGMMfDS9yOkcPrHRQon0bQ")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://killua:<password>@cluster0.nr34b.mongodb.net/?retryWrites=true&w=majority")

INDEX_ID = int(getenv("INDEX_ID", "-1001774600331"))
UPLOADS_ID = int(getenv("UPLOADS_ID", "-1001768494729"))

STATUS_ID = int(getenv("STATUS_ID", "2"))
SCHEDULE_ID = int(getenv("SCHEDULE_ID", "3"))

CHANNEL_TITLE = getenv("CHANNEL_TITLE", "Anime Uploads Channel")
INDEX_USERNAME = getenv("INDEX_USERNAME", "@Anime_Upload_Index")
UPLOADS_USERNAME = getenv("UPLOADS_USERNAME", "@Anime_Uploads")
