from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def test_chrome_driver_working():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")  # Disable GPU rendering
    driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.google.com")
    print("Page title:", driver.title)
    #driver.quit()

def test_chrome_driver():
    options = webdriver.ChromeOptions()
    #options.add_argument(r"user-data-dir=C:\\Users\\mail2\\AppData\\Local\\Google\\Chrome\\User Data")  # Parent directory
    options.add_argument(r"profile-directory=Default")  # Specific profile
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--remote-debugging-port=9222")


    driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.google.com")
    print("Page title:", driver.title)

def test_chrome_driver_notworking():
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
    driver.get("https://www.google.com")
    print("Page title:", driver.title)

test_chrome_driver()
