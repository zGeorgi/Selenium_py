from selenium import webdriver

driver = webdriver.Chrome(executable_path="/home/georgi/chromedriver/chromedriver")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

boxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

print(len(boxes))

for box in boxes:
    # get the attribute value
    print(box.get_attribute("value"))
    box.click()
    #-- check if the box have a tick
    assert box.is_selected()

radio_buttons = driver.find_elements_by_name("radioButton")
print(len(radio_buttons))
radio_buttons[2].click()
print(radio_buttons[2].is_selected())
driver.close()
