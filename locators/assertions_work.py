from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/home/georgi/chromedriver/chromedriver")

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_xpath("//input[@type='submit']").click()

msg = driver.find_element_by_css_selector("[class*='alert-success']").text
driver.close()
assert "success" in msg
