import socks
from telethon import TelegramClient
from telethon.sessions import StringSession

from utils.load_env import env

if env.PROXY:
    PROXY = dict(proxy_type=socks.SOCKS5, addr='127.0.0.1', port=1080)

if env.SESSION_STRING:
    SESSION_NAME = StringSession(env.SESSION_STRING)

client = TelegramClient(session=SESSION_NAME, api_id=env.API_ID, api_hash=env.API_HASH, proxy=PROXY)
