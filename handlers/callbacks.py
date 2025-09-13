from telethon import events

from client import client


@client.on(events.CallbackQuery(data=b"btn_ping"))
async def ping_callback(event):
    await event.answer("🏓 پونگ!")
    await event.edit(f"کاربر {event.sender_id} روی دکمه کلیک کرد.")

@client.on(events.CallbackQuery(data=b"btn_info"))
async def info_callback(event):
    await event.answer("دریافت اطلاعات...")
    await event.respond("🔹 این یه تست ربات CLI هست.")
