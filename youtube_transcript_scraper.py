from pytube import Playlist
import requests
from bs4 import BeautifulSoup

def get_video_ids_from_playlist(playlist_url):
    """
    Get all video IDs from a YouTube playlist using pytube.

    Args:
        playlist_url (str): URL of the YouTube playlist.

    Returns:
        list: List of video IDs.
    """
    try:
        playlist = Playlist(playlist_url)
        video_ids = [video.video_id for video in playlist.videos]
        return video_ids
    except Exception as e:
        raise Exception(f"Error fetching video IDs: {e}")

def get_transcript_from_website(video_id):
    """
    Scrape the transcript of a YouTube video using https://youtubetranscript.com/.

    Args:
        video_id (str): ID of the YouTube video.

    Returns:
        str: Transcript text.
    """
    url = f"https://youtubetranscript.com/?v={video_id}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching transcript for video {video_id}: {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')
    transcript_div = soup.find('div', {'id': 'demo'})

    if not transcript_div:
        return f"Transcript not found for video {video_id}."

    transcript_text = transcript_div.get_text(separator=" ").strip()
    return transcript_text
