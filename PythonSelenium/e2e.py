import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path="F:\\Tool EXE-Raksha\\Selenium Drivers\\Drivers\\chromedriver.exe", options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice")
driver.find_element_by_css_selector("a[href*='shop']").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")

product_selected =[]
Total_product_cart =[]

for product in products:
    product_selected.append(product.find_element_by_xpath("div/h4").text)
    productname = product.find_element_by_xpath("div/h4").text
    if productname in 'Blackberry':
        product.find_element_by_xpath("div/button").click()
print(product_selected)
time.sleep(2)
driver.find_element_by_css_selector("a[class*='btn-primary']").click()

productNameinCart = driver.find_elements_by_xpath("//div[@class='media']/div/h4")
for product_in_cart in productNameinCart:
    Total_product_cart.append(product_in_cart.text)
print(Total_product_cart)
assert set(product_selected) and set(Total_product_cart)

driver.find_element_by_css_selector("button[class*='btn-success']").click()
driver.find_element_by_id("country").send_keys("in")

wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

driver.find_element_by_link_text("India").click()
privacy_policy = driver.find_element_by_css_selector("div[class*='checkbox'] label")
privacy_policy.click()
##driver.find_element_by_css_selector("button[class*='btn-info']").click()
## assert privacy_policy.is_selected()
driver.find_element_by_css_selector("input[class*='btn-lg']").click()
time.sleep(2)
success_messg = driver.find_element_by_css_selector("div[class*='alert-success']").text

assert "Success!" in success_messg

driver.get_screenshot_as_file("scr.png")



