# Discord Smart Downloader 🚀

[![Python](https://img.shields.io/badge/Python-3.9+-blue)](https://www.python.org/)
[![Discord.py](https://img.shields.io/badge/Discord.py-2.3.2-blue)](https://discordpy.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

**Discord Smart Downloader** is a fast, lightweight Discord bot for downloading videos from multiple platforms using slash commands, with direct delivery to users’ DMs. Designed to be simple, reliable, and ready for deployment.

---

## ⚡ Features

- ✅ Slash command support for easy interaction
- 🎛️ Quality selection via dropdown menu (Best/Worst)
- 📩 DM-only delivery to keep channels clean
- 🧹 Automatic file cleanup to save storage
- 🌐 Multi-platform video support via **yt-dlp**  
  *(YouTube, TikTok, Instagram, Twitter/X, and more)*
- 🛠 Lightweight and easy to deploy anywhere
- 🔒 Privacy-focused: Downloads sent directly to users

---

## 📝 Commands

| Command       | Description                        |
|---------------|------------------------------------|
| `/download`   | Download a video directly to your DM |
| `/ping`       | Check bot status and latency       |

**Example usage:**
```bash
/download url:https://example.com/video quality:best


⚙️ Installation

Clone the repository:

git clone https://github.com/nawaf133/discord-smart-downloader.git
cd discord-smart-downloader


Install dependencies:

pip install -r requirements.txt


Create a .env file in the project root:

DISCORD_TOKEN=YOUR_BOT_TOKEN_HERE


Run the bot:

python bot.py


💡 Make sure Python 3.9+ and FFmpeg are installed on your system for full functionality.

🖥 Supported Platforms

YouTube

TikTok

Instagram

Twitter (X)

Any platform supported by yt-dlp

🧾 Ownership & License

Developed and maintained by @_I42
Licensed under the MIT License – free to use and modify, but original credit must remain.

🎯 Notes

Users must have DMs enabled to receive downloads.

Large files may take longer depending on platform and network speed.

All downloads are automatically deleted after sending to prevent storage issues.

Made with ❤️ for simple, efficient, and practical video downloading on Discord.
