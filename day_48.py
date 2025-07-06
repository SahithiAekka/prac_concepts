from selenium import webdriver 
# webdriver module lets you control browsers like Chrome 



# Keepin gchrome browser open after program finishes 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Setting up with selenium 
driver= webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.amazon.com")



# Locator strategies: "https://www.selenium.dev/documentation/webdriver/elements/locators/"













# driver.close() # closes the active tab  
# driver.quit() #closes the entire browser 
