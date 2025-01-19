from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def generate_metadata_with_chatgpt(story):
    """Generates YouTube video metadata using ChatGPT."""
    driver = webdriver.Chrome()
    driver.get("https://chat.openai.com/")
    time.sleep(20)  # Wait for manual login if needed

    # Locate the input box and send the prompt
    input_box = driver.find_element(By.TAG_NAME, "textarea")
    prompt = (
        f"I have created a YouTube video using images and the below story. "
        f"Can you create a title and description for this YouTube video to rank high? "
        f"I would like the description to be packed with keywords and SEO to help me rank high "
        f"in my niche and among search results. My niche is Short stories. "
        f"My target viewers are kids, children, teens, and parents looking for short stories.\n\n{story}"
    )
    input_box.send_keys(prompt)
    input_box.send_keys("\n")  # Simulate pressing Enter
    time.sleep(30)  # Wait for the response to load

    # Locate and extract the response
    metadata = driver.find_element(By.CSS_SELECTOR, ".chat-message-content").text
    driver.quit()
    return metadata