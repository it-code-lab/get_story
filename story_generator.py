from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def enhance_story_with_chatgpt(transcript):
    driver = webdriver.Chrome()
    driver.get("https://chat.openai.com/")

    try:
        # Wait for manual login if needed
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.TAG_NAME, "textarea"))
        )

        # Locate and interact with the input box
        input_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
        )
        input_box.click()  # Focus on the text area
        prompt = (
            f"Please enhance the below story and make it interesting in around 500 words. "
            f"Change the name of the characters and storyline if needed to make it original. "
            f"Also suggest a title for the story.\n\n{transcript}"
        )
        input_box.send_keys(prompt)
        input_box.send_keys("\n")  # Simulate pressing Enter

        # Wait for the response to load
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".chat-message-content"))
        )
        response = driver.find_element(By.CSS_SELECTOR, ".chat-message-content").text
    except Exception as e:
        print(f"Error interacting with ChatGPT: {e}")
        response = None
    finally:
        driver.quit()

    return response
