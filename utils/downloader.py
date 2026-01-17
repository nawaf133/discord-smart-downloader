# Downloader Module
# Developed by @_I42

import yt_dlp
import os
import uuid

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_video(url, quality):
    filename = f"{uuid.uuid4()}.mp4"
    path = os.path.join(DOWNLOAD_DIR, filename)

    ydl_opts = {
        "outtmpl": path,
        "format": quality,
        "quiet": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return path
