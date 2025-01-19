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

def generate_metadata_with_chatgpt(story):
    """Generates YouTube video metadata using ChatGPT."""
    #driver = webdriver.Chrome()
    driver = setup_driver_with_profile()
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