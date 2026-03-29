# To save the audio as an MP3, you will also need FFmpeg installed on your system, as it handles the actual conversion from the raw video/audio stream into the MP3 format.

import yt_dlp

def download_playlist_mp3(playlist_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        # Updated output template for playlists
        'playlist_items': '1::1',  # Specify the range of videos to download (e.g., 34-40)
        'outtmpl': '%(playlist_title)s/%(playlist_title)s_%(playlist_index)s.%(ext)s',
        'noplaylist': False,  # Ensure it downloads the entire playlist
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl: # type: ignore
            print(f"Starting playlist download...")
            ydl.download([playlist_url])
            print("\nFinished! Your MP3s are organized in a folder named after the playlist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
url = input("Enter the YouTube Playlist URL: ")
download_playlist_mp3(url)