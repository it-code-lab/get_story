from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver_with_profile():
    options = webdriver.ChromeOptions()
    #options.add_argument(r"user-data-dir=C:\\Users\\mail2\\AppData\\Local\\Google\\Chrome\\User Data")  # Update with your Chrome profile path
    options.add_argument(r"profile-directory=Default")  # Use your specific Chrome profile (e.g., 'Default' or 'Profile 1')
    options.add_argument("--disable-blink-features=AutomationControlled")  # Hide automation flags
    options.add_argument("--no-sandbox")  # Prevent sandbox issues
    options.add_argument("--disable-gpu")  # Disable GPU rendering
    options.add_argument("--disable-dev-shm-usage")  # Handle resource issues on some systems
    options.add_argument("--remote-debugging-port=9222")  # Allow debugging
    
    # Initialize the ChromeDriver with the service wrapper
    driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()), options=options)
    return driver

def generate_images_with_storyteller(story):
    """Generates photorealistic images for a story using an image generation tool."""
    scenes = story.split("\n")[:10]  # Extract up to 10 scenes
    image_urls = []

    driver = setup_driver_with_profile()
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