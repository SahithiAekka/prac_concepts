from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
import time

# Keep Chrome browser open after program finishes 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the form 
driver.get("https://secure-retreat-92358.herokuapp.com/")

# Find the first name, last name, and email fields 
first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

# Filling out the form 
first_name.send_keys("Sahithi")
last_name.send_keys("Aekka")
email.send_keys("sahithiaekka@gmail.com")

# Locate the sign up button then click on it 
submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()