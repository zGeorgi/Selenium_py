import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="/home/georgi/chromedriver/chromedriver")
#--------- wait up to 5 seconds per line to be execute and display---------
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(3)
add_to_bassket = driver.find_elements_by_xpath("//button[text()='ADD TO CART']")

for butt in add_to_bassket:
    butt.click()

driver.find_element_by_css_selector("a[class='cart-icon'] img").click()
driver.find_element_by_xpath("//button[text()= 'PROCEED TO CHECKOUT']").click()
# time.sleep(3)
driver.find_element_by_css_selector("div[class='promoWrapper'] input").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
msg = driver.find_element_by_css_selector(".promoInfo").text

assert "Code applied ..!" in msg
