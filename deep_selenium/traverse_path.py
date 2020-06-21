import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="/home/georgi/chromedriver/chromedriver")
driver.get("https://rahulshettyacademy.com/seleniumPractise")
list_first_page=[]
list_second_page =[]

wait = WebDriverWait(driver, 8)

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")

time.sleep(3)
add_to_bassket = driver.find_elements_by_xpath("//button[text()='ADD TO CART']")

for butt in add_to_bassket:
    list_first_page.append(butt.find_element_by_xpath("parent::div/parent::div/h4").text)
    butt.click()

print(list_first_page)
driver.find_element_by_css_selector("a[class='cart-icon'] img").click()
driver.find_element_by_xpath("//button[text()= 'PROCEED TO CHECKOUT']").click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='promoWrapper'] input")))
names = driver.find_elements_by_css_selector("p.product-name")

for name in names:
    list_second_page.append(name.text)

print(list_second_page)
assert list_second_page == list_first_page

originalAmount = driver.find_element_by_css_selector(".discountAmt").text
driver.find_element_by_css_selector("div[class='promoWrapper'] input").send_keys("rahulshettyacademy")

driver.find_element_by_css_selector(".promoBtn").click()
# -- xpath for extract the sum from table
#------//table[@class='cartTable']/tr/td[5]/p
prices = driver.find_elements_by_xpath("//table[@class='cartTable']/tr/td[5]/p")
suma = 0.0
for price in prices:
    suma = suma + float(price.text)
print(suma)
assert suma == float(originalAmount)

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo" )))
discountAmount = driver.find_element_by_css_selector(".discountAmt").text

print(float(originalAmount))
print(float(discountAmount))
assert float(originalAmount) > float(discountAmount)

msg = driver.find_element_by_css_selector(".promoInfo").text

assert "Code applied ..!" in msg
