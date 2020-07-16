from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="/home/georgi/chromedriver/chromedriver")
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

action = ActionChains(driver)
#action.move_to_element(driver.find_element_by_css_selector("input[id='double-click']")).double_click().perform()
#context click for is right button
action.context_click(driver.find_element_by_css_selector("input[id='double-click']")).perform()
action.double_click(driver.find_element_by_css_selector("input[id='double-click']")).perform()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()