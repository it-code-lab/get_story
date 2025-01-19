from youtube_transcript_api import YouTubeTranscriptApi

def get_transcripts_from_playlist(playlist_url):
    """
    Get transcripts for all videos in a YouTube playlist.
    
    Args:
        playlist_url (str): URL of the YouTube playlist.

    Returns:
        dict: A dictionary where keys are video titles and values are their transcripts.
    """
    import requests
    from urllib.parse import urlparse, parse_qs

    # Extract playlist ID
    playlist_id = parse_qs(urlparse(playlist_url).query).get('list', [None])[0]
    if not playlist_id:
        raise ValueError("Invalid playlist URL")

    # Get video IDs in the playlist
    api_url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId={playlist_id}&key=YOUR_YOUTUBE_API_KEY"
    response = requests.get(api_url)
    if response.status_code != 200:
        raise Exception(f"Error fetching playlist videos: {response.text}")

    data = response.json()
    transcripts = {}

    for item in data['items']:
        video_id = item['snippet']['resourceId']['videoId']
        video_title = item['snippet']['title']

        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            transcripts[video_title] = " ".join([t['text'] for t in transcript])
        except Exception as e:
            transcripts[video_title] = f"Error: {e}"

    return transcripts