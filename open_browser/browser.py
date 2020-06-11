from selenium import webdriver

# path to executable file to open Chrome
#driver = webdriver.Firefox(executable_path="/home/georgi/geckodriver/geckodriver")
driver = webdriver.Chrome(executable_path="/home/georgi/chromedriver/chromedriver")
#open the url
driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
print(driver.title)
#  print the url on current page
print(driver.current_url)
#driver.close()  # only current window will be closed
driver.get("https://rahulshettyacademy.com/AutomationPractice")
#driver.minimize_window()
driver.back()
driver.refresh()
driver.close()
driver.quit() # close all windows
