from telethon import events
from telethon.tl.types import InputBotInlineMessageText, InputBotInlineResult

from client import client


@client.on(events.InlineQuery)
async def inline_handler(event):
    query = event.query.string or ""

    if query == "ping":
        result = InputBotInlineResult(
            id="1",
            type="article",
            title="پاسخ پینگ",
            description="یه پیام ساده",
            send_message=InputBotInlineMessageText("🏓 پونگ!")
        )
        await event.answer([result])
