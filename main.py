from telethon import TelegramClient, events
import os
import asyncio

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
session_name = "railway_session"

client = TelegramClient(session_name, api_id, api_hash)

TARGET_KEYWORDS = [
    "🔥 @Chatkeeperbot - number one group management service in Telegram",
    "Welcome to Catton Community"
]

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    sender = await event.get_sender()
    if not sender.bot:
        return

    text = event.raw_text
    for keyword in TARGET_KEYWORDS:
        if keyword in text:
            try:
                await event.delete()
                print("✅ Deleted message:", text)
            except Exception as e:
                print("❌ Error deleting:", e)
            break

async def main():
    await client.connect()
    if not await client.is_user_authorized():
        print("❌ Session invalid or not uploaded!")
        return
    print("✅ Connected! Bot is running...")
    await client.run_until_disconnected()

asyncio.run(main())
