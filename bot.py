# Discord Smart Downloader
# Developed by @_I42
# GitHub Project: discord-smart-downloader
# License: MIT

import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from utils.downloader import download_video
from utils.cleaner import cleanup_file

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

class QualitySelect(discord.ui.Select):
    def __init__(self, url):
        self.url = url
        options = [
            discord.SelectOption(label="Best Quality", value="best"),
            discord.SelectOption(label="Worst Quality", value="worst"),
        ]
        super().__init__(
            placeholder="Choose video quality",
            options=options,
            min_values=1,
            max_values=1
        )

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message("Downloading...", ephemeral=True)

        file_path = download_video(self.url, self.values[0])

        try:
            await interaction.user.send(file=discord.File(file_path))
            cleanup_file(file_path)
        except:
            await interaction.followup.send(
                "❌ Failed to send file. Make sure your DMs are open.",
                ephemeral=True
            )

class QualityView(discord.ui.View):
    def __init__(self, url):
        super().__init__(timeout=60)
        self.add_item(QualitySelect(url))

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")

@bot.tree.command(name="download", description="Download a video and receive it in DM")
@app_commands.describe(url="Video URL")
async def download(interaction: discord.Interaction, url: str):
    await interaction.response.send_message(
        "Select video quality:",
        view=QualityView(url),
        ephemeral=True
    )

@bot.tree.command(name="ping", description="Check bot status")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong!", ephemeral=True)

bot.run(TOKEN)
