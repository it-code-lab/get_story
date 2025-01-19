from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
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

def get_transcript(video_url):
    driver = setup_driver_with_profile()
    driver.get(f"https://youtubetranscript.com/?v={video_url.split('v=')[-1]}")
    
    try:
        # Wait up to 10 seconds for the element to appear
        transcript_element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "demo"))
        )
        transcript = transcript_element.text
        print(transcript);
    except Exception as e:
        print(f"Error retrieving transcript: {e}")
        transcript = None
    finally:
        driver.quit()
    
    return transcript
