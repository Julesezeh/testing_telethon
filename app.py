import os
from telethon import TelegramClient, events, sync
from dotenv import load_dotenv

load_dotenv()

apiId = os.getenv("API_ID")
apiHash = os.getenv("API_HASH")


client = TelegramClient("session_name",api_id=apiId,api_hash=apiHash)
client.start()