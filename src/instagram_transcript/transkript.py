# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "faster-whisper",
#     "yt-dlp",
#     "av<19",
# ]
# ///

import os
import yt_dlp
from faster_whisper import WhisperModel


def reel_transkript_ucretsiz(url):
    audio_path = "reel_sesi.mp3"

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "reel_sesi.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "128",
            }
        ],
        "quiet": True,
    }

    print("1. Reels sesi indiriliyor...")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("2. Metne dönüştürülüyor...")
    model = WhisperModel("base", device="cpu", compute_type="int8")
    segments, info = model.transcribe(audio_path, beam_size=5)

    transkript = " ".join([segment.text for segment in segments])

    if os.path.exists(audio_path):
        os.remove(audio_path)

    return transkript.strip()


if __name__ == "__main__":
    url = "https://www.instagram.com/p/De_2bznR1RR/"
    cikti_dosyasi = "transkript.txt"

    metin = reel_transkript_ucretsiz(url)

    # Transkripti UTF-8 formatında metin dosyasına yaz
    with open(cikti_dosyasi, "w", encoding="utf-8") as f:
        f.write(metin)

    print(f"\nİşlem tamamlandı! Transkript '{cikti_dosyasi}' dosyasına kaydedildi.")
