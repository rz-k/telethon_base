from telethon import events

from client import client


@client.on(events.Raw)
async def log_raw_update(event):
    print(event)
    print("—" * 60)
