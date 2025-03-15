from youtube_transcript_api import YouTubeTranscriptApi

def _getYoutubeTranscript(videoId):

    if not isinstance(videoId,str):
        raise TypeError("`videoId` should be a string!")

    ytt_api = YouTubeTranscriptApi()
    fetched_transcript = ytt_api.fetch(videoId, preserve_formatting=True)

    return (videoId, fetched_transcript.to_raw_data())

