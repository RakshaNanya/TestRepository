import time
from logging import exception

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="F:\\Tool EXE-Raksha\\Selenium Drivers\\Drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
radiobtn = driver.find_elements_by_css_selector("input[type='radio']")

try:
    for radio in radiobtn:
        radio.click()
        print("Failed")

except exception as e:
    print(e)

finally:
    radiobtn[2].click()
    time.sleep(2)
    driver.close()