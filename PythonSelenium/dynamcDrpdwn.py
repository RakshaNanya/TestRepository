import time
from logging import exception

from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:\\Tool EXE-Raksha\\Selenium Drivers\\Drivers\\chromedriver.exe")
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
try:
    driver.find_element_by_css_selector("div[class*='searchCity']").click()
    driver.find_element_by_css_selector("input[class*='autosuggest__input']").send_keys("del")
    time.sleep(3)
    # city = driver.find_elements_by_css_selector("div[class*='suggestions-container'] div:nth-child(1) ul li div div p[class*='blackText']")
    city = driver.find_elements_by_css_selector("p[class*='font14']")
    print("{}{}".format("total count= ", len(city)))
    for i in city:
        print(i.text)
except exception as e:
    print(e)

finally:
    driver.close()

