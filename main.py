import os
import yt_dlp

def download_vimeo_video(url, output_folder="downloaded_videos"):
    # Create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # yt-dlp configuration
    options = {
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',  # Best available quality
    }
    
    with yt_dlp.YoutubeDL(options) as ydl:
        try:
            print(f"Downloading: {url}")
            ydl.download([url])
            print("Download completed successfully.\n")
        except Exception as e:
            print(f"Error downloading the video {url}: {e}\n")

if __name__ == "__main__":
    url = input("Enter the Vimeo video URL: ")
    download_vimeo_video(url)