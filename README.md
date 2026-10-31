# 🎙️ Instagram Reels Transcript Generator

Instagram Reels videolarındaki konuşmaları **tamamen ücretsiz**, yerel ve hızlı bir şekilde yazıya (transkript) dönüştüren Python tabanlı bir araçtır.

Ses indirme işlemi için [`yt-dlp`](https://github.com/yt-dlp/yt-dlp), konuşmayı metne çevirme (Speech-to-Text) işlemi için ise optimize edilmiş [`faster-whisper`](https://github.com/SYSTRAN/faster-whisper) modeli kullanılır.

---

## 🚀 Özellikler

- **%100 Ücretsiz & Çevrimdışı (Offline):** Herhangi bir ücretli API anahtarı (OpenAI vb.) veya abonelik gerektirmez.
- **Hafif ve Hızlı:** Standart Whisper modellerine kıyasla 4 kata kadar daha az RAM ve CPU tüketen `faster-whisper` altyapısı kullanılır.
- **Otomatik Dil Tespiti:** Türkçe dahil onlarca dili otomatik tanır.
- **UTF-8 Çıktı Desteği:** Türkçe karakter kaybı olmadan sonucu doğrudan `.txt` dosyasına kaydeder.
- **Modern Paket Yönetimi:** [`uv`](https://github.com/astral-sh/uv) ile izole, hatasız ve ışık hızında çalışma desteği.

---

## 📁 Proje Yapısı

```text
instagram-transcript/
├── src/
│   └── instagram_transcript/
│       ├── __init__.py
│       ├── transkript.py      # Ana çalıştırma scripti
│       └── transkript.txt     # Oluşturulan transkript çıktısı
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
└── uv.lock
```

---

## 🛠️ Gereksinimler

### 1. `ffmpeg` Kurulumu (Zorunlu)
Ses dönüştürme adımları için sisteminizde `ffmpeg` kurulu olmalıdır:

- **Windows:**
  ```powershell
  winget install Gyan.FFmpeg
  ```
- **macOS:**
  ```bash
  brew install ffmpeg
  ```
- **Linux (Ubuntu/Debian):**
  ```bash
  sudo apt update && sudo apt install -y ffmpeg
  ```

### 2. `uv` Paket Yöneticisi
Proje bağımlılıklarını yönetmek için `uv` önerilir:
```bash
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## 💻 Kullanım

1. **Repoyu klonlayın:**
   ```bash
   git clone https://github.com/kullanici-adiniz/instagram-transcript.git
   cd instagram-transcript
   ```

2. **Reels URL'sini Belirleyin:**  
   `src/instagram_transcript/transkript.py` dosyasını açıp dilediğiniz Instagram Reels bağlantısını `url` değişkenine yapıştırın:
   ```python
   url = "https://www.instagram.com/p/De_2bznR1RR/"
   ```

3. **Çalıştırın:**  
   Herhangi bir sanal ortam kurmanıza gerek kalmadan `uv` ile doğrudan çalıştırabilirsiniz:
   ```bash
   uv run src/instagram_transcript/transkript.py
   ```

İşlem tamamlandığında aynı klasörde **`transkript.txt`** adında metin dosyası oluşturulacaktır.

---

## ⚠️ Karşılaşılabilecek Durumlar

- **PyAV / Metadata Hatası:** `faster-whisper` kütüphanesinin kararlı çalışabilmesi adına `av<19` sürüm kısıtlaması script bağımlılıklarına dahil edilmiştir.
- **Instagram Bot Koruması:** Reels içeriği herkese açık olmalıdır. Gizli profiller veya Instagram hız sınırına takılma durumlarında script içerisindeki `ydl_opts` ayarına tarayıcı çerezleri (`'cookiesfrombrowser': ('chrome', )`) eklenebilir.

---

## 📄 Lisans

Bu proje [MIT](LICENSE) lisansı ile lisanslanmıştır.