from selenium import webdriver

driver = webdriver.Chrome(executable_path="/home/georgi/chromedriver/chromedriver")

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("hello JS")
 # selenium can't catch the value like this
print(driver.find_element_by_name("name").text)

print(driver.find_element_by_name("name").get_attribute("value"))
#------ execute js code-----
value = driver.execute_script("return document.getElementsByName('name')[0].value")
print(value)

shop_button = driver.find_element_by_css_selector("a[href*='shop']")
# ----- can take more than two parameters-------
# execute_script("argument[index].<js action on argument>" , argument[0], argument[1]...)
driver.execute_script("arguments[0].click();" , shop_button)

#----------js scroll example -----------
# only possible with JS (not supported from Selenium)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#driver.close()