from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:\\Tool EXE-Raksha\\Selenium Drivers\\Drivers\\chromedriver.exe")
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
driver.find_element_by_css_selector("div[class*='searchCity']").click()
driver.find_element_by_css_selector("input[class*='autosuggest__input']").send_keys("del")
city = driver.find_elements_by_css_selector("div[class*='suggestions-container'] div:nth-child(1) ul li")
for i in city:
    print(i.text)
driver.close()
