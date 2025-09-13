# Telegram CLI Bot Template

A clean, modular, and production-ready template for building Telegram CLI bots using [Telethon](https://github.com/Lonami/Telethon).  
This project follows modern Python practices with `pyproject.toml`, `uv`, environment configuration, logging, and a scalable handler structure.

Perfect for automation, server monitoring, personal bots, or reusable bot templates across projects.

---

## 🧱 Project Structure

```
.
├── client.py                   # Shared TelegramClient with config & proxy support
├── handlers/                   # Modular event handlers
│   ├── commands.py             # Commands like !ping, !help
│   ├── callbacks.py            # Handle button clicks (CallbackQuery)
│   ├── inline.py               # Inline query responses
│   ├── triggers.py             # React to keywords (e.g. "hello", "thanks")
│   ├── chat_actions.py         # User join/leave, title changes
│   └── raw_updates.py          # Log all raw updates (debug only)
├── main.py                     # Entry point and bot runner
├── pyproject.toml              # Modern dependency management
├── README.md                   # This file
├── utils/
│   ├── load_env.py             # Load settings from .env.ini
│   └── logger.py               # Simple colored logging
└── uv.lock                     # Lock file for deterministic installs
```

---

## ⚙️ Configuration: `.env.ini`

First, copy the example config:

```bash
cp .env.ini.example .env.ini
```

Then edit `.env.ini` with your credentials:

```ini
[Bot]
API_ID=1234
API_HASH=abcsdewjj2j3uuu3u3u3uu3u3u
SESSION_NAME=cli_bot
# Optional: Replace with your string session. If set, SESSION_NAME is ignored.
SESSION_STRING=

[Proxy]
# Optional: Format = host:port (e.g. 127.0.0.1:1080)
PROXY=127.0.0.1:1080

[Other]
ADMIN_ID=219171508
```

> 🔐 **Important**: `.env.ini` is already in `.gitignore`. Never commit it!

---

## 📦 Installation (using `uv`)

This project uses [`uv`](https://github.com/astral-sh/uv) — a fast Python installer and resolver.

### 1. Install `uv` (if not installed)
```bash
pip install uv
```

### 2. Install dependencies
```bash
uv sync
```

> ✅ Uses `pyproject.toml` — no need for `requirements.txt`.

---

## ▶️ Run the Bot

```bash
python main.py
```

On first run:
- If `SESSION_STRING` is empty, you’ll be asked for your phone number.
- A session file (`cli_bot.session`) will be created.
- The bot will start and respond to commands.

---

## 🔐 Session Management

### Option 1: File-based Session (`SESSION_NAME`)
- Used when `SESSION_STRING` is empty.
- Stores session in a local `.session` file.
- First-time login required.

### Option 2: String Session (`SESSION_STRING`)
- Paste your existing string session here.
- Ideal for servers, Docker, or headless environments.
- No login needed on restart.

> To generate a string session, use tools like [Telethon String Session Generator](https://repl.it/@Bluegasm/TelethonStringSessionGenerator).

---

## 🌐 Proxy Support

If behind a firewall or restricted network, set `PROXY=host:port` in `.env.ini`.

```ini
PROXY=127.0.0.1:1080
```

> Requires `PySocks` (already in `pyproject.toml`).  
> Only **SOCKS5** proxies are supported by Telethon.

---

## 🧩 Handler Modules

Each handler file listens to specific events:

| Module | Purpose |
|-------|--------|
| `commands.py` | Commands like `!ping`, `!help` |
| `callbacks.py` | Button click responses |
| `inline.py` | Inline queries (`@yourbot search`) |
| `triggers.py` | Auto-replies to keywords like "hi", "thanks" |
| `chat_actions.py` | Welcome messages, user joins |
| `raw_updates.py` | Debug: log every raw Telegram update |

Add new modules easily — just import them in `main.py`.

---

## 🛠️ Example: Add a New Handler

1. Create `handlers/media.py`:
```python
from client import client
from telethon import events
from utils.logger import info

@client.on(events.NewMessage(media=True))
async def handle_media(event):
    info(f"Media received from {event.sender_id}")
    await event.reply("📁 فایل دریافت شد!")
```

2. Import in `main.py`:
```python
from handlers import media
```

Done!

---

## 📝 Logging

Uses a simple, clean logger from `utils.logger`:

```python
from utils import logger

logger.info("Bot started")
logger.error("Something went wrong")
```

Output format:
```
[14:23:05] INFO: Bot started
[14:23:06] ERROR: Something went wrong
```

---

## 💡 Tips

- Use `raw_updates.py` during development to inspect incoming update structures.
- Comment out unused handler imports in `main.py` to disable them.
- For production, remove `raw_updates.py` import — it logs too much.
- Store `SESSION_STRING` securely — it gives full account access.

---

## 📚 Dependencies

Defined in `pyproject.toml`:

```
telethon==1.34.0
pysocks ; extra == "proxy"
```

Install optional proxy support:
```bash
uv pip install 'telethon-cli-bot[proxy]'
```

---

## 🙏 Credits

Built with ❤️ using [Telethon](https://github.com/Lonami/Telethon).  
Designed for reusability, clarity, and ease of deployment.

---

## 📬 Feedback & Contributions

Welcome! Open an issue or PR for improvements, bug fixes, or new features.