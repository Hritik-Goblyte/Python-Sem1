import os
import uuid
from pytube import YouTube

def download_youtube_video():
    print("---------------------------------------")
    print("                                       ")
    print("-- Welcome To YouTube Video Downloader --")
    print("                                       ")
    print("---------------------------------------")
    print("                                       ")

    url = input("Enter the YouTube video URL: ")

    yt = YouTube(url)

    try:
        yt.bypass_age_gate()  # Try bypassing age gate if the video is restricted
    except Exception as e:
        print(f"Error bypassing age gate: {e}")

    # Selecting the highest resolution MP4 stream
    stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()

    output_dir = "yt-videos"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = f"{uuid.uuid4()}.mp4"
    output_path = os.path.join(output_dir, filename)

    # Downloading the video to the correct location
    stream.download(output_path=output_dir, filename=filename)

    print(f"Video downloaded and saved to {output_path}")

download_youtube_video()

