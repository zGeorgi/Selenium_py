import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="/home/georgi/chromedriver/chromedriver")
driver.get("https://rahulshettyacademy.com/seleniumPractise")
#--------- Explicit Wait -------------
# make object for class "WebDriverWait(driver, 5)"
wait = WebDriverWait(driver, 8)

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
#wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[text()='ADD TO CART']")))
time.sleep(3)
add_to_bassket = driver.find_elements_by_xpath("//button[text()='ADD TO CART']")

for butt in add_to_bassket:
    butt.click()

driver.find_element_by_css_selector("a[class='cart-icon'] img").click()
driver.find_element_by_xpath("//button[text()= 'PROCEED TO CHECKOUT']").click()



# "expected_conditions" import
# "By"  import
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='promoWrapper'] input")))

driver.find_element_by_css_selector("div[class='promoWrapper'] input").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo" )))
msg = driver.find_element_by_css_selector(".promoInfo").text

assert "Code applied ..!" in msg
