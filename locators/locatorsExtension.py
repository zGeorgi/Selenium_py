from selenium import webdriver

driver = webdriver.Chrome(executable_path="/home/georgi/chromedriver/chromedriver")
driver.get("https://login.salesforce.com/?locale=uk")
# CSS find element by id "#"
driver.find_element_by_css_selector("#username").send_keys("georgi")
# CSS find element by classname "."
driver.find_element_by_css_selector(".password").send_keys("parola")
#clear the input
driver.find_element_by_css_selector(".password").clear()

driver.find_element_by_link_text("Forgot Your Password?").click()
#catch all elements with text 'Cancel' in them
driver.find_element_by_xpath("//*[text()='Cancel']").click()
print(driver.find_element_by_xpath("//div[@id='usernamegroup']/label").text)
print(driver.find_element_by_css_selector("div[id='usernamegroup'] label").text)
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(4)").text)
