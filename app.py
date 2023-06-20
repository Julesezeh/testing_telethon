import os
import socks
import sqlite3
import threading
from datetime import date
import json
import os
from dotenv import load_dotenv
from flask import Flask
from telethon import TelegramClient, events, sync
from dotenv import load_dotenv

load_dotenv()

apiId = os.getenv("API_ID")
apiHash = os.getenv("API_HASH")

# Proxy = (socks.SOCKS5, '145.239.85.58', '9300')


app = Flask(__name__)


# (optional) set some logging to see what is happening under the hood
# logging.basicConfig(
#     filename="apps.log",
#     filemode="a",
#     level=logging.INFO,
#     format="%(asctime)s [%(filename)s:%(lineno)d]|%(levelname)s|%(message)s",
# )


def background_task():
    # database configs
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    # cursor.execute("CREATE TABLE log (user_id, created_at)")

    # 2. define an update handler (every time an update is received, it will execute it)
    # this will print in console every new message received

    def message_handler(event):
        print(event)

    while True:
        # Initiate the client
        client = TelegramClient("session_name", api_id=apiId, api_hash=apiHash)

        # Login to the client
        client.start()


@app.before_first_request
def start_background_task():
    # Start the background task in a separate thread
    background_thread = threading.Thread(target=background_task())
    background_thread.start()


@app.route("/", methods=["GET"])
def index():
    me = {"name": "Jules", "phone_number": "090"}
    return json.dumps(me)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
