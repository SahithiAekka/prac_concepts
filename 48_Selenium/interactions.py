from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
import time

# Keep Chrome browser open after program finishes 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the Wikipedia main page
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Optional: wait for page to load (prevents race condition)
time.sleep(1)

# Get the article count element by its CSS selector (ID = #articlecount)
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount")
# print(article_count.text)

# The below lets you click on the screen (uncomment to use)
# article_count.click()  

# Find the "Search" <input> by its 'name' attribute — used for searching
search = driver.find_element(By.NAME, value="search")

# Sending keyboard input to Selenium
search.send_keys("Python", Keys.ENTER)
#Alternatively: search.submit()  # triggers the form submission without hitting Enter

