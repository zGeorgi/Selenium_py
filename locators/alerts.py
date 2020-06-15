from selenium import webdriver

driver = webdriver.Chrome(executable_path="/home/georgi/chromedriver/chromedriver")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_css_selector("#name").send_keys("Optionn777")
driver.find_element_by_css_selector("#alertbtn").click()

#-----------  swich to alert object
alert = driver.switch_to.alert

alert_text = alert.text

assert "Optionn777" in alert_text
#----------- press "ok" to alert-------
alert.accept()
#-----------press "cancel"-----
alert.dismiss()