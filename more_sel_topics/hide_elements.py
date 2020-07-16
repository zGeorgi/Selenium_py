
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/home/georgi/chromedriver/chromedriver")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#------- the "is_displayed()" return true or false if the eleemnt is displayed
assert driver.find_element_by_css_selector("#displayed-text").is_displayed()

driver.find_element_by_id("hide-textbox").click()

# continue the program if logical answer is "false"
assert not driver.find_element_by_css_selector("#displayed-text").is_displayed()