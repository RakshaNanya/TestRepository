from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:\\Tool EXE-Raksha\\Selenium Drivers\\Drivers\\chromedriver.exe")
driver.get("https://login.salesforce.com/")
driver.maximize_window()
driver.find_element_by_id("username").send_keys("Raksha")
driver.find_element_by_id("password").send_keys("abc")
driver.find_element_by_xpath("//input[contains(@id,'Login')]").click()
mesage = driver.find_element_by_xpath("//form[@id='login_form']/div[1]").text
print(mesage)
assert "can't log in" in mesage
driver.close()