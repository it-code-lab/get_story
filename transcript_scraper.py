from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

def get_transcript(video_url):
    driver = webdriver.Chrome()
    driver.get(f"https://youtubetranscript.com/?v={video_url.split('v=')[-1]}")
    
    try:
        # Wait up to 10 seconds for the element to appear
        transcript_element = WebDriverWait(driver, 10).until(
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
