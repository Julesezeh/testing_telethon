import os
import socks 
from telethon import TelegramClient, events, sync
from dotenv import load_dotenv

load_dotenv()

apiId = os.getenv("API_ID")
apiHash = os.getenv("API_HASH")

Proxy = (socks.SOCKS5, '145.239.85.58', '9300')
client = TelegramClient("session_name",api_id=apiId, api_hash=apiHash,proxy=Proxy)
client.start()