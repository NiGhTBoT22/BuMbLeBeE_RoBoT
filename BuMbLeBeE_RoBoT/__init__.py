from telethon import TelegramClient
from telethon.sessions import StringSession
import time
import os, logging
from logging import basicConfig, getLogger, INFO
"""BuMbLeBeE_RoBoT"""
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
 )
logging.basicConfig( format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)

StartTime = time.time()

SES = os.environ.get("SES")
URL = os.environ.get("DB_URL")
TOKEN = os.environ.get("TOKEN")
OWNER_ID = os.environ.get("OWNER_ID")
API_KEY = os.environ.get("API_KEY")
API_HASH = os.environ.get("API_HASH ")

ubot = TelegramClient(StringSession(SES), API_KEY API_HASH)
tbot = TelegramClient(None, API_KEY, API_HASH)
