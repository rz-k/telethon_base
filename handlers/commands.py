import platform

from telethon import events

from client import client


@client.on(events.NewMessage(pattern=r'^!help$'))
async def help_cmd(event: events.NewMessage.Event):
    text = """
📌 دستورات:

!ping → تست
!sysinfo → اطلاعات سیستم
!help → این پیام
    """.strip()
    await event.reply(text)

@client.on(events.NewMessage(pattern=r'^!ping$'))
async def ping(event):
    await event.reply("🏓 پونگ!")

@client.on(events.NewMessage(pattern=r'^!sysinfo$'))
async def sysinfo(event):
    info = f"🖥️ {platform.system()} - {platform.node()}"
    await event.reply(info)
