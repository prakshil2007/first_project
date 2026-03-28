from selenium import webdriver

# Requires a webdriver (like chromedriver) installed
driver = webdriver.Chrome() 
driver.get("https://www.youtube.com")

print(driver.title)
driver.quit()