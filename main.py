import asyncio  # noqa: I001

from client import client
from handlers import (
    commands,  # noqa: F401
    callbacks,  # noqa: F401
    inline,  # noqa: F401
    triggers,  # noqa: F401
    chat_actions, # noqa: F401
    raw_updates  # noqa: F401
)

async def main():
    await client.start()
    print("✅ ربات فعال است.")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
