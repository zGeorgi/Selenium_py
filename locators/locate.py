from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/home/georgi/chromedriver/chromedriver")
# open the webpage
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# driver.find_element_by_class_name("form-control").send_keys("Georgi")
# send_keys enter value in the element
driver.find_element_by_css_selector("input[name='name']").send_keys("georgi")
driver.find_element_by_name('email').send_keys("gzayakov1@gmail.com")

driver.find_element_by_id("exampleCheck1").click()
# handel dropdown menu  with select tag
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
# indexes start from 0
dropdown.select_by_index(0)
# if the "value" argument is present
# dropdown.select_by_value()

driver.find_element_by_xpath("//input[@type='submit']").click()
# "text" grab the text from the element

# print((driver.find_element_by_xpath("//*[contains(text(),'alert-successs')]")).text)
# print(driver.find_element_by_css_selector("[class*='alert-success']").text)
# print(driver.find_element_by_class_name("alert-success").text)
