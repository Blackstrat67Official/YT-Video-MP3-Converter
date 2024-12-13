import yt_dlp
import os

def download_youtube_video_and_extract_audio(youtube_url, output_directory):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_directory, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Scaricando il video e estraendo l'audio...")
            ydl.download([youtube_url])
            print("Audio MP3 scaricato con successo.")
    except Exception as e:
        print(f"Errore: {e}")

if __name__ == "__main__":
    youtube_link = input("Inserisci il link del video di YouTube: ")
    output_dir = input("Inserisci la directory di output (default: cartella corrente): ") or "."
    download_youtube_video_and_extract_audio(youtube_link, output_dir)
