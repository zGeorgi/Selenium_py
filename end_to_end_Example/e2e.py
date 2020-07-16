import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="/home/georgi/chromedriver/chromedriver")

driver.get("https://rahulshettyacademy.com/angularpractice/")

shop_button = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();", shop_button)

item_name = driver.find_element_by_link_text("Blackberry")

print(item_name.text)
# //a[text()='Blackberry']/parent::h4/parent::div/parent::div/div[@class='card-footer']/button
item_name.find_element_by_xpath("parent::h4/parent::div/parent::div/div[@class='card-footer']/button").click()

driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()


assert "Blackberry" == driver.find_element_by_xpath("//h4/a").text
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()

driver.find_element_by_css_selector("#country").send_keys("ita")

wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Italy")))
driver.find_element_by_link_text("Italy").click()

driver.find_element_by_xpath("//label[@for='checkbox2']").click()
driver.find_element_by_css_selector("input[value='Purchase']").click()

msg = driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text

assert "Success" in msg

driver.get_screenshot_as_file("screen.png")
