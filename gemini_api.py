import requests

def enhance_story_with_gemini(api_key, story):
    """
    Enhance a story using Gemini API.

    Args:
        api_key (str): API key for Gemini.
        story (str): Original story text.

    Returns:
        str: Enhanced story text.
    """
    url = "https://generativeai.googleapis.com/v1beta1/models/text-bison:generateText"  
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    # Prepare the payload
    payload = {
        "prompt": (
            "I have a short kids story. I need you to help me enhance and recreate it for a YouTube video. "
            f"Here is the story: {story}. \n\n"
            "**Considering my niche (short stories) and target audience (kids, children, teens, and parents), "
            "please provide the following:**\n"
            "1. **Enhanced and recreated story:** A new version of the story with changed character names and storyline "
            "if needed (to make the story original and avoid any copyrights). The new story should be around 500 words, "
            "suitable for a YouTube video targeting children and families. \n"
            "2. **YouTube Title:** A catchy and engaging title for a YouTube video based on the recreated story, appealing to "
            "both children and parents. \n"
            "3. **YouTube Description:** A concise and informative description of the YouTube video, including a brief summary "
            "of the story, highlighting its suitability for families, and encouraging viewers to subscribe and share. \n"
            "4. **YouTube Tags:** A list of relevant keywords and phrases to help the video rank well on YouTube, considering "
            "search terms used by parents and children looking for short stories (e.g., 'kids stories', 'bedtime stories', "
            "'children's books', 'family stories', 'short stories for kids', 'educational stories', 'moral stories')."
        ),
        "temperature": 0.7,
        "max_tokens": 1200
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json().get("output", "No output found")
    else:
        raise Exception(f"Error from Gemini API: {response.status_code} - {response.text}")

def generate_video_metadata(api_key, story):
    """
    Generate metadata for YouTube video using Gemini API.

    Args:
        api_key (str): API key for Gemini.
        story (str): Enhanced story text.

    Returns:
        dict: A dictionary containing title, description, and tags.
    """
    url = "https://gemini.googleapis.com/v1/your-endpoint"  # Replace with actual endpoint
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "input": (
            f"I have created YouTube video using images and above story. Can you Please create title, description, "
            f"and tags for this YouTube video to rank high? I would like this description to be packed full of keywords "
            f"and SEO to help me rank high in my niche and among search results. \n\n"
            f"My niche is Short stories. \n"
            f"My Target viewers are kids, children, teens, and parents looking for short stories. \n\n{story}"
        )
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error from Gemini API: {response.status_code} - {response.text}")