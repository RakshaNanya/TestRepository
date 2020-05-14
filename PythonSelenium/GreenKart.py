import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="F:\\Tool EXE-Raksha\\Selenium Drivers\\Drivers\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()
# implicit wait- It wasits for the maximum time provided to load the object. If Object is loaded
# before the max time then it resumes the exccution
driver.implicitly_wait(6)
# Enter ber in search field.
driver.find_element_by_css_selector("input[type='search']").send_keys("ber")
time.sleep(2)
AddToKart = driver.find_elements_by_xpath("//div[@class='product-action']/button")
len(AddToKart)
# find the length after entering to search field
assert len(AddToKart) == 3
for Add in AddToKart:
    Add.click()
    time.sleep(2)
# Click all the button to add to the cart
driver.find_element_by_xpath("//img[@alt='Cart']").click()
time.sleep(2)
totalCart = driver.find_elements_by_xpath("//div[contains(@class,'active')]/div/div/ul/li")
# check whether 3 products are added in the cart
assert len(totalCart) == 3
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(2)

# Enter the promoCode
driver.find_element_by_css_selector(".promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()

print(driver.find_element_by_css_selector(".promoInfo").text)




