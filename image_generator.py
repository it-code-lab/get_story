from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def generate_images_with_storyteller(story):
    """Generates photorealistic images for a story using an image generation tool."""
    scenes = story.split("\n")[:10]  # Extract up to 10 scenes
    image_urls = []

    driver = webdriver.Chrome()
    driver.get("https://your_image_storyteller_tool.com/")  # Replace with actual URL

    for scene in scenes:
        input_box = driver.find_element(By.ID, "prompt_input")
        input_box.clear()
        input_box.send_keys(f"Photorealistic scene: {scene}")
        input_box.send_keys("\n")
        time.sleep(10)  # Wait for image generation
        
        image_url = driver.find_element(By.CLASS_NAME, "generated-image").get_attribute("src")
        image_urls.append(image_url)

    driver.quit()
    return image_urls