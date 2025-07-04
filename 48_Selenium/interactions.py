from selenium import webdriver
from selenium.webdriver.common.by import By 

# Keep Chrome browser open after program finishes 
chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

# Creat and configure the chrome webdriver
driver = webdriver.Chrome(options= chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count= driver.find_element(By.CSS_SELECTOR, value="#articlecount")

print(article_count.text)
