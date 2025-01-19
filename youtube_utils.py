from pytube import Playlist

def get_video_urls(playlist_url):
    """Fetches video URLs from a YouTube playlist."""
    playlist = Playlist(playlist_url)
    return playlist.video_urls