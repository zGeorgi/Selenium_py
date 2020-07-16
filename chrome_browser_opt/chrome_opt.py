from selenium import webdriver
#---https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--ignore--certificate-errors')

driver = webdriver.Chrome(executable_path="/home/georgi/chromedriver/chromedriver", options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)