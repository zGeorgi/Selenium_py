import time

from selenium import webdriver


driver = webdriver.Chrome(executable_path="/home/georgi/chromedriver/chromedriver")
driver.get("https://www.makemytrip.com/")

driver.find_element_by_css_selector("div[class='fsw_inner '] div label").click()
driver.find_element_by_css_selector("div[role='combobox'] input").send_keys("del")
#next two line are doing the same job
#cities= driver.find_elements_by_css_selector("ul[role='listbox'] li p ")
cities = driver.find_elements_by_css_selector("p[class*='blackText']")

print(len(cities))
for city in cities:
    if city.text == "Delhi, India":
        city.click()
        break
# stop the program for 3 seconds
time.sleep(3)

driver.find_element_by_xpath("//p[text()='Mumbai, India']").click()