import yt_dlp
import ffmpeg

def _getYoutubeMp3Audio(youtube_url,output_path = "audio.wav"):
    ydl_opts = {"format": "bestaudio"}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        stream_url = info["url"]
    
    audio, err = (
        ffmpeg
        .input(stream_url)
        .output("pipe:", format='wav', acodec='pcm_s16le')
        .run(capture_stdout=True)
    )

    with open('audio.wav', 'wb') as f:
        f.write(audio)

    return 1
