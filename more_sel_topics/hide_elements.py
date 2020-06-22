
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="/home/georgi/chromedriver/chromedriver")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#------- the "is_displayed()" return true or false is eleemnt is displayed
assert driver.find_element_by_css_selector("#displayed-text").is_displayed()

driver.find_element_by_id("hide-textbox").click()

assert not driver.find_element_by_css_selector("#displayed-text").is_displayed()