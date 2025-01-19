import requests

def enhance_story(api_key, story):
    """
    Enhance a story using Gemini API.

    Args:
        api_key (str): API key for Gemini.
        story (str): Original story text.

    Returns:
        str: Enhanced story text.
    """
    url = "https://gemini.googleapis.com/v1/your-endpoint"  # Replace with actual endpoint
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "input": f"Please Enhance below story and make interesting in around 500 words. Change the name of the characters and storyline if needed to make it original. \n\n{story}"
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