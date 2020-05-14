from selenium import webdriver # base package.
# Every browser exposes an excutable browser.
# a file is provided.
driver = webdriver.Chrome(executable_path='F:\\Tool EXE-Raksha\\Selenium Drivers\\Drivers\\chromedriver.exe')
# driver = webdriver.Firefox(executable_path='F:\\Tool EXE-Raksha\\Selenium Drivers\\Drivers\\geckodriver.exe')
# driver.get("https://rahulshettyacademy.com/#/index")  # get method will help u to hit on the link given
# driver.get("https://sso.teachable.com/secure/9521/users/sign_in?clean_login=true&reset_purchase_session=1")
driver.maximize_window()
print(driver.title)
# make sure that u land on the proper page.
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/#/practice-project")
# driver.back()
# driver.refresh()

driver.find_element_by_name("name").send_keys("Raksha")
driver.find_element_by_css_selector("input[id='email']").send_keys("rakshananya@gmail.com")

driver.find_element_by_xpath("//input[@name='commit']").click()
print(driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[1]/div/div").text)
driver.close()
