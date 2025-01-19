import time
from pytube import Playlist
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import xml.etree.ElementTree as ET
import re

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

def get_transcript_from_website_Notworking_DueTo_Async_Refresh(video_id):
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
    # wait 20 seconds
    #time.sleep(20)  # Wait for the page to load
    if not transcript_div:
        return f"Transcript not found for video {video_id}."

    transcript_text = transcript_div.get_text(separator=" ").strip()
    print(transcript_text)
    return transcript_text


#Not working with Selenium
def get_transcript_from_website(video_id):
    """
    Scrape the transcript of a YouTube video using https://youtubetranscript.com/ with Selenium.

    Args:
        video_id (str): ID of the YouTube video.

    Returns:
        str: Transcript text.
    """
    url = f"https://youtubetranscript.com/?v={video_id}"
    
    # Setup Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode (no browser UI)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Open the page
        driver.get(url)

        # Wait for the transcript content to update dynamically (max wait: 30 seconds)
        transcript_div = WebDriverWait(driver, 30).until(
            EC.text_to_be_present_in_element((By.ID, "demo"), "Loading captions...")
        )
        
        # Retrieve the transcript text
        transcript_element = driver.find_element(By.ID, "demo")
        transcript_text = transcript_element.text.strip()

        print(f"Transcript fetched successfully for video {video_id}: {transcript_text}")
        return transcript_text

    except Exception as e:
        print(f"Error fetching transcript for video {video_id}: {e}")
        return f"Transcript not found for video {video_id}."

    finally:
        driver.quit()

def get_transcript_from_backend(video_id):
    """
    Fetch the transcript of a YouTube video using the backend API.

    Args:
        video_id (str): ID of the YouTube video.

    Returns:
        str: Transcript text.
    """
    url = f"https://youtubetranscript.com/?server_vid2={video_id}"
    headers = {
        "accept": "application/xml, text/xml, */*; q=0.01",
        "accept-language": "en-US,en;q=0.9,hi;q=0.8,fr;q=0.7",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest",
        "referer": f"https://youtubetranscript.com/?v={video_id}",
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(f"Received transcript for video {video_id}")
        # Parse the response based on the format (assuming XML in this case)
        transcript_text = response.text.strip()  # Adjust parsing based on the actual format
        cleaned_story = clean_transcript(transcript_text)
        return cleaned_story

    except requests.exceptions.RequestException as e:
        return f"Error fetching transcript: {e}"

def clean_transcript(transcript_xml):
    """
    Cleans the YouTube transcript XML to extract readable story text.

    Args:
        transcript_xml (str): The raw XML transcript content.

    Returns:
        str: A cleaned and formatted story text.
    """
    try:
        # Parse the XML content
        root = ET.fromstring(transcript_xml)

        # Extract the text from each <text> tag and join them into a single story
        story_lines = [element.text for element in root.findall(".//text") if element.text]
        story = " ".join(story_lines)

        # Replace unwanted placeholders or patterns
        story = story.replace("[Music]", "").replace("&apos;", "'").strip()

        # Add sentence casing and paragraph formatting
        story = format_story_text(story)

        return story
    except ET.ParseError as e:
        return f"Error parsing transcript XML: {e}"

def format_story_text(story):
    """
    Formats the story text by applying sentence casing and paragraph breaks.

    Args:
        story (str): Raw story text.

    Returns:
        str: Formatted story text.
    """
    # Split into sentences using punctuation
    sentences = re.split(r'(\.|\?|!)\s+', story)

    # Recombine sentences with proper casing
    formatted_sentences = []
    for sentence in sentences:
        if sentence.strip():
            formatted_sentences.append(sentence.strip().capitalize())

    # Combine sentences into paragraphs (5 sentences per paragraph)
    paragraphs = []
    for i in range(0, len(formatted_sentences), 5):
        paragraphs.append(" ".join(formatted_sentences[i:i+5]))

    # Join paragraphs with double line breaks
    formatted_story = "\n\n".join(paragraphs)

    return formatted_story

# Example usage
if __name__ == "__main__":
    video_id = "4KkvSY6ILBc"  # Replace with the YouTube video ID
    transcript = get_transcript_from_backend(video_id)
    #transcript = get_transcript_from_website(video_id)
    print(transcript)


