from telethon import events

from client import client


@client.on(events.ChatAction)
async def welcome_new_member(event):
    if event.user_joined or event.user_added:
        users = ", ".join(f"[{u.first_name}](tg://user?id={u.id})" for u in event.users)
        await event.reply(f"👋 خوش آمدید، {users}!")

@client.on(events.ChatAction(func=lambda e: e.user_left or e.user_kicked))
async def user_left(event):
    user = event.user
    await event.reply(f"👤 کاربر [{user.first_name}](tg://user?id={user.id}) رفته.")
