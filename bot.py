import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
session_string = os.environ.get("SESSION_STRING")

async def main():
    client = TelegramClient(StringSession(session_string), api_id, api_hash)

    @client.on(events.NewMessage)
    async def handler(event):
        print("Mesaj geldi:", event.raw_text)

    await client.start()
    print("Userbot çalışıyor...")
    await client.run_until_disconnected()

asyncio.run(main())
