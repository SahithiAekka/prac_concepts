# Upcominge events of python website 
# printout a dic that has event dates and names 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Step 1: Setup the Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Step 2: Open the target website
driver.get("https://www.python.org/")

# Step 3: Locate event dates using CSS selector
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")

# Step 4: Locate event names using refined CSS selector
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

# Step 5: Build dictionary from extracted data
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

# Step 6: Print the final dictionary
print(events)

# Step 7: Optional – Close the browser after execution
driver.quit()