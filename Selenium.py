from selenium import webdriver
from selenium.common.keys import Keys

browser = webdriver.Firefox()
# for chrome
#browser = webdriver.Firefox()
browser.get("https://www.google.co.in/")
elem = browser.find_element_by_name("q")
elem.send_keys("Nameof the site)
elem.send_keys(Keys.RETURN)
browser.quit()
