import yt_dlp

def download_video():
    url = input("Enter the YouTube video URL: ").strip()
    path = input("Enter the download path (e.g., C:\\Users\\YourName\\Downloads): ").strip()


    ydl_opts = {
        'outtmpl': f'{path}/%(title)s.%(ext)s', 
        'format': 'mp4',                         
        'quiet': False,                          
        'noplaylist': True                       
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n✅ Video downloaded successfully!")
        print(f"Saved to: {path}")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    download_video()
