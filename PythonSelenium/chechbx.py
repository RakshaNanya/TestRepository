import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="F:\\Tool EXE-Raksha\\Selenium Drivers\\Drivers\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
checkboxes = driver.find_elements_by_css_selector("input[type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    print(checkbox.get_attribute("value"))
    time.sleep(3)
    if checkbox.get_attribute("value") == "option1":
        checkbox.click()
        assert checkbox.is_selected()
        time.sleep(5)
time.sleep(5)
driver.close()

