from selenium import webdriver

driver = webdriver.Chrome(executable_path="/home/georgi/chromedriver/chromedriver")
# open the webpage
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# driver.find_element_by_class_name("form-control").send_keys("Georgi")
#send_keys enter value in the element
driver.find_element_by_css_selector("input[name='name']").send_keys("georgi")
driver.find_element_by_name('email').send_keys("gzayakov1@gmail.com")

driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_xpath("//input[@type='submit']").click()
# "text" grab the text from the element

print((driver.find_element_by_xpath("//*[contains(@class,'alert-successs')]")).text)
#print(driver.find_element_by_css_selector("[class*='alert-success']").text)
#print(driver.find_element_by_class_name("alert-success").text)