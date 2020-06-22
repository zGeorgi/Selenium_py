import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="/home/georgi/chromedriver/chromedriver")
driver.get("https://www.familysearch.org/en/")
seq = driver.find_elements_by_tag_name('iframe')
print(len(seq))
time.sleep(3)

# iframme
myframe = driver.find_elements_by_tag_name('iframe')[0]

driver.switch_to.frame(myframe)
driver.find_element_by_link_text("Agree and Proceed").click()
driver.switch_to.default_content()
time.sleep(3)

# ActionsChain class to handle the actions
actions = ActionChains(driver)
# -------always perform should be call on the end to be execute the action
actions.move_to_element(driver.find_element_by_xpath("//button[text() = 'Search']")).click().perform()

driver.find_element_by_link_text("Genealogies").click()
