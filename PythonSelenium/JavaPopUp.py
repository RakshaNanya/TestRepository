import time
from logging import exception

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="F:\\Tool EXE-Raksha\\Selenium Drivers\\Drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
Name = "Raksha"
driver.find_element_by_css_selector("#name").send_keys(Name)
driver.find_element_by_css_selector("#alertbtn").click()
time.sleep(2)
alert = driver.switch_to.alert  # switch to alert mode to get the java pop up
alert_Text = alert.text         # get the text from the alert
print(alert_Text)
assert Name in alert_Text       # Compare it with the required text.
time.sleep(2)
alert.accept()
time.sleep(2)

driver.find_element_by_css_selector("#confirmbtn").click()
time.sleep(2)
alert_Text2 = alert.text
print(alert_Text2)
alert.dismiss()


