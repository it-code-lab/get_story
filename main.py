from youtube_utils import get_video_urls
from transcript_scraper import get_transcript
from story_generator import enhance_story_with_chatgpt
from image_generator import generate_images_with_storyteller
from metadata_generator import generate_metadata_with_chatgpt
from utils import save_data

def automate_youtube_story_workflow(playlist_url):
    video_urls = get_video_urls(playlist_url)

    for video_url in video_urls:
        transcript = get_transcript(video_url)
        story = enhance_story_with_chatgpt(transcript)
        images = ""
        #images = generate_images_with_storyteller(story)
        metadata = generate_metadata_with_chatgpt(story)
        save_data(story, images, metadata)
        print(f"Processed video: {video_url}")

if __name__ == "__main__":
    playlist_url = "https://www.youtube.com/playlist?list=PLBLx6pEVoUoby0tcR0FdlVsXoLTyia9ad"
    automate_youtube_story_workflow(playlist_url)