from youtube_transcript_scraper import get_video_ids_from_playlist, get_transcript_from_backend
from gemini_api import enhance_story_with_gemini
from excel_writer import save_results_to_excel
import os
from dotenv import load_dotenv

secrets_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'secrets.env')
load_dotenv(secrets_path)

# Access the Gemini API key
API_KEY = os.getenv('GEMINI_API_KEY')

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Ensure it is set in secrets.env.")

print(f"Loaded API Key: {API_KEY[:4]}...")  # Partially print the key for debugging

def automate_youtube_story_workflow_Old(playlist_url, api_key, output_file):
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
            print(f"processing video {video_id}")
            transcript = get_transcript_from_backend(video_id)
            if "Transcript not found" in transcript:
                print(f"Skipping video {video_id}: {transcript}")
                continue

            enhanced_data = enhance_story_with_gemini(api_key, transcript)
            results.append({
                "Video ID": video_id,
                "Enhanced Story": enhanced_data.get("enhanced_story"),
                "Title": enhanced_data.get("title"),
                "Description": enhanced_data.get("description"),
                "Tags": ", ".join(enhanced_data.get("tags", []))
            })
        except Exception as e:
            print(f"Error processing video {video_id}: {e}")

    save_results_to_excel(results, output_file)

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
            print(f"Processing video {video_id}")
            transcript = get_transcript_from_backend(video_id)
            if "Transcript not found" in transcript:
                print(f"Skipping video {video_id}: {transcript}")
                continue

            # Make Gemini API call
            response_data = enhance_story_with_gemini(api_key, transcript)

            # Extract specific fields
            content = response_data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
            if not content:
                print(f"No content found in Gemini response for video {video_id}")
                continue

            # Parse structured content
            lines = content.split("\n\n")
            enhanced_story = next((line for line in lines if line.startswith("## 1. Enhanced")), "").replace("## 1. Enhanced and Recreated Story:", "").strip()
            title = next((line for line in lines if line.startswith("## 2. YouTube Title:")), "").replace("## 2. YouTube Title:", "").strip()
            description = next((line for line in lines if line.startswith("## 3. YouTube Description:")), "").replace("## 3. YouTube Description:", "").strip()
            tags = next((line for line in lines if line.startswith("## 4. YouTube Tags:")), "").replace("## 4. YouTube Tags:", "").strip()

            # Store results
            results.append({
                "Video ID": video_id,
                "Enhanced Story": enhanced_story,
                "Title": title,
                "Description": description,
                "Tags": tags,
                "Full Response": response_data  # Store the full response for future reference
            })

        except Exception as e:
            print(f"Error processing video {video_id}: {e}")

    save_results_to_excel(results, output_file)
    
# Example usage
if __name__ == "__main__":
    playlist_url = "https://www.youtube.com/playlist?list=PLBLx6pEVoUoby0tcR0FdlVsXoLTyia9ad"
    api_key = API_KEY
    output_file = "output.xlsx"
    automate_youtube_story_workflow(playlist_url, api_key, output_file)
