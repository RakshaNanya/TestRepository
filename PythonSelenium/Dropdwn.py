
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="F:\\Tool EXE-Raksha\\Selenium Drivers\\Drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
print(driver.title)
drpdwn = Select(driver.find_element_by_id("dropdown-class-example"))
drpdwn.select_by_index(1)
drpdwn.select_by_visible_text("Option3")
drpdwn.select_by_value("option1")

driver.close()