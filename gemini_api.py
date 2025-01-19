import requests
import os
from dotenv import load_dotenv

def enhance_story_with_gemini(api_key, story):
    """
    Enhance a story using Gemini API.

    Args:
        api_key (str): API key for Gemini.
        story (str): Original story text.

    Returns:
        str: Enhanced story text.
    """
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {
        "Content-Type": "application/json"
    }
    
    # Prepare the payload
    payload = {
        "contents": [{
            "parts": [{
                "text": (
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
                )
            }]
        }]
    }
    
    # Send the request to Gemini API
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Return the response from the API
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

if __name__ == "__main__":
    # Load API key from secrets file
    secrets_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'secrets.env')
    load_dotenv(secrets_path)

    # Access the Gemini API key
    API_KEY = os.getenv('GEMINI_API_KEY')

    # Original story
    oldstory = """
    In a magical forest filled with whispering trees and playful winds, lived two best friends: Milo, a clever mouse, and Nia, a curious rabbit. They spent their days exploring every nook and cranny of their lush home, sharing adventures, and curling up under an ancient hollow tree at night to recount their escapades. Their friendship was unbreakable, built on trust and mutual care.

    One day, a mischievous squirrel named Felix arrived in the forest. Felix had a penchant for causing chaos, pulling pranks that started as harmless fun but soon escalated into dangerous antics. The forest animals quickly learned to steer clear of him, but Milo and Nia, kindhearted as they were, tolerated Felix—until one day, his prank went too far.

    Felix rigged a vine to send Milo and Nia tumbling into a thorny bush. Covered in scratches, the friends confronted him, demanding an apology. Felix grudgingly complied but relished the attention his antics brought. Milo and Nia, though forgiving, decided to avoid him from then on. This rejection infuriated Felix, and he vowed revenge.

    As winter approached, food in the forest grew scarce. Felix, always scheming, discovered a hidden corn crib and saw an opportunity for his next prank. He visited Milo and Nia, claiming he’d found an abundant food source. Desperate and skeptical, the friends hesitated, but hunger drove them to trust him.

    The trio embarked on their journey to the corn crib. Upon arrival, they found a narrow hole leading inside. Felix neglected to mention an important detail: they would need to monitor their size while feasting, or risk getting stuck. As they devoured the corn, Felix slyly slipped away now and then to ensure he could still fit through the escape hole.

    Milo and Nia, unaware of the trick, ate to their hearts' content until they heard distant footsteps. Alarmed, they rushed to escape. Felix slipped through the hole effortlessly, but Milo and Nia found themselves trapped, their bellies too round to fit. Felix grinned smugly from the other side, mocking them before vanishing into the forest.

    Terrified, Milo and Nia awaited their fate. Instead of the corn crib’s owner, a wounded guard cat appeared. Seeing their plight, Milo and Nia tended to the cat’s injuries. Touched by their kindness, the cat let them stay the night and escape in the morning once their bellies had flattened.

    Weeks later, a heavy snowfall blanketed the forest. As Milo and Nia warmed themselves by their fire, a loud crash echoed in the distance. Investigating, they found Felix’s burrow had caved in, trapping him inside. Other animals ignored his cries, but Milo and Nia paused, hearing Felix’s faint plea for help.

    “My friends, I wronged you both and don’t deserve your kindness,” Felix called out, his voice trembling. “But please, forgive me.”

    Milo and Nia hesitated, then began digging through the snow with their sharp claws. Hours later, they freed Felix. Overwhelmed with gratitude, Felix promised to abandon his pranks and earn their friendship. From that day on, Felix kept his word, and the three became inseparable, their bond forged in forgiveness and redemption.
    """

    # Enhance the story using the Gemini API
    newstory = enhance_story_with_gemini(API_KEY, oldstory)

    # Print the enhanced story
    print(newstory)
