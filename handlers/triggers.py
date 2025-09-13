import re

from telethon import events

from client import client


@client.on(events.NewMessage(pattern=r'^(سلام|hi|hello)$', func=lambda e: e.is_private))
async def hello(event: events.NewMessage.Event):
    await event.reply("👋 سلام! چطوری؟")

@client.on(events.NewMessage(pattern=re.compile(r'.*ممنون.*', re.IGNORECASE)))
async def thanks(event):
    await event.reply("😊 خواهش می‌کنم!")

@client.on(events.NewMessage(pattern='!admin', func=lambda e: e.sender_id == 123456789))
async def only_admin(event: events.NewMessage.Event):
    await event.reply("شما ادمین هستید.")
