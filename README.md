# 🎥 Video Downloader for Vimeo Platform

A simple and efficient script to download Vimeo videos using `yt-dlp`. Users can enter a Vimeo URL via the console, and the video is downloaded in the best available quality.

## 🚀 Features
- ✅ **Best quality** (bestvideo + bestaudio)
- ✅ Saves to **`downloaded_videos/`**
- ✅ **Minimal setup** (Python + yt-dlp)
- ✅ Works on **Windows, macOS, and Linux**

## 📌 Installation & Usage
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/video-downloader-for-vimeo.git
   cd video-downloader-for-vimeo
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the script and enter a Vimeo URL**
   ```bash
   python main.py
   ```
4. The video will be **saved automatically** in the `downloaded_videos/` folder 🎬

## 🐳 Docker Support
Run the tool inside a **Docker container**:
```bash
docker build -t vimeo-downloader .
docker run -it -v "$(pwd)/downloaded_videos:/app/downloaded_videos" vimeo-downloader
```

## 🤝 Contribute
Feel free to **open issues, submit PRs**, or suggest new features. Your contributions are welcome! 🎉
