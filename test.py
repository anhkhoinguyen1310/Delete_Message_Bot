from telethon import TelegramClient
from telethon.sessions import StringSession


with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("Here is your string session:")
    print(client.session.save())
