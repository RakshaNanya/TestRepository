import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="F:\\Tool EXE-Raksha\\Selenium Drivers\\Drivers\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()
list1 = []
list2 = []
AllVeggies = []
SearchedVegies =[]

AllVegies1 = driver.find_elements_by_class_name("product-name")
for i in AllVegies1:
    AllVeggies.append(i.text)

driver.find_element_by_css_selector("input[type='search']").send_keys("ber")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='product-action']/button")))
time.sleep(2)

SearchedVegies1 = driver.find_elements_by_class_name("product-name")
for i in SearchedVegies1:
    SearchedVegies.append(i.text)
# Set method to compare the two list
assert set(AllVeggies) & set(SearchedVegies)
AddToKart = driver.find_elements_by_xpath("//div[@class='product-action']/button")

print(len(AddToKart))
# find the length after entering to search field

assert len(AddToKart) == 3
for Add in AddToKart:
    list1.append(Add.find_element_by_xpath("parent::div/parent::div/h4").text)
    Add.click()
print(list1)

# Click all the button to add to the cart
driver.find_element_by_xpath("//img[@alt='Cart']").click()

totalCart = driver.find_elements_by_xpath("//div[contains(@class,'active')]/div/div/ul/li")
# check whether 3 products are added in the cart
assert len(totalCart) == 3
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
# before entering the promocode make sure that the page is loaded.

wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
# Enter the promoCode
vegies = driver.find_elements_by_class_name("product-name")

for vegy in vegies:
    list2.append(vegy.text)
print(list2)

assert list1 == list2

sumAmmount = driver.find_elements_by_xpath("//table[@class='cartTable']/tr/td[5]/p")
summation = 0
for totalsum in sumAmmount:
    summation = summation + int(totalsum.text)
print(summation)
driver.find_element_by_css_selector(".promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))

afterDiscnt = driver.find_element_by_css_selector("span.discountAmt")
assert float(afterDiscnt.text) < summation
print(driver.find_element_by_css_selector(".promoInfo").text)

driver.close()




