from selenium import webdriver

driver = webdriver.Chrome(executable_path='F:\\Tool EXE-Raksha\\Selenium Drivers\\Drivers\\chromedriver.exe')
driver.maximize_window()
driver.get("https://login.salesforce.com/")
print(driver.find_element_by_xpath("//div[@class='inputgroup']/label").text)
print(driver.find_element_by_xpath("//form[@name='login']/label").text)

driver.close()