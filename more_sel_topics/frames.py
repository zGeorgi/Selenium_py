# ---- driver object can access only the html and not the inbuild frame---
# <iframe>, <frameset>, <frame> are the tags for frame declaretion
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/home/georgi/chromedriver/chromedriver")
driver.get("https://the-internet.herokuapp.com/iframe")

# next method get argument <frame id> or <frame name> or <indexvalue>
# move <driver> in the frame
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("I change the content!")

# switch <driver> to parent html
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)
