from youtube_transcript_scraper import get_video_ids_from_playlist, get_transcript_from_website
from gemini_api import enhance_story, generate_video_metadata
from excel_writer import save_results_to_excel

def automate_youtube_story_workflow(playlist_url, api_key, output_file):
    """
    Automate the workflow to get transcripts, enhance stories, and generate metadata.

    Args:
        playlist_url (str): URL of the YouTube playlist.
        api_key (str): Gemini API key.
        output_file (str): Path to save the Excel file.
    """
    video_ids = get_video_ids_from_playlist(playlist_url)
    results = []

    for video_id in video_ids:
        try:
            transcript = get_transcript_from_website(video_id)
            if "Transcript not found" in transcript:
                print(f"Skipping video {video_id}: {transcript}")
                continue

            enhanced_story = enhance_story(api_key, transcript)
            metadata = generate_video_metadata(api_key, enhanced_story)
            results.append({
                "Video ID": video_id,
                "Enhanced Story": enhanced_story,
                "Title": metadata.get("title"),
                "Description": metadata.get("description"),
                "Tags": ", ".join(metadata.get("tags", []))
            })
        except Exception as e:
            print(f"Error processing video {video_id}: {e}")

    save_results_to_excel(results, output_file)

# Example usage
if __name__ == "__main__":
    playlist_url = "https://www.youtube.com/playlist?list=PLBLx6pEVoUoby0tcR0FdlVsXoLTyia9ad"
    api_key = "YOUR_GEMINI_API_KEY"
    output_file = "output.xlsx"
    automate_youtube_story_workflow(playlist_url, api_key, output_file)
