from selenium import webdriver

driver = webdriver.Chrome(executable_path="/home/georgi/chromedriver/chromedriver")
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element_by_link_text("Click Here").click()
#------ return list with windows-------------
child_window = driver.window_handles

driver.switch_to.window(child_window[1])
print(driver.find_element_by_tag_name("h3").text)

#------ swich to parent window---------
driver.switch_to.window(driver.window_handles[0])
print(driver.find_element_by_tag_name("h3").text)

driver.close()