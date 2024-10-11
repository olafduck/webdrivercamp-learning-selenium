from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()

url = "https://www.ebay.com/"
search_box = "//input[@id='gh-ac']"
search_button = "//input[@id='gh-btn']"

# Task 1
# driver.get(url)
# print(driver.title)
# driver.quit()

# Task 2
# driver.get(url)
# wait = WebDriverWait(driver, 10)
# wait.until(expected_conditions.visibility_of_element_located((By.XPATH, search_box)))
# print(driver.title)
# driver.quit()

# Task 3
# driver.get(url)
# wait = WebDriverWait(driver, 10)
# wait.until(expected_conditions.visibility_of_element_located((By.XPATH, search_box)))
# print(driver.title)
# driver.find_element(By.XPATH, search_box).send_keys("women watch")
# driver.find_element(By.XPATH, search_button).click()
# driver.quit()

# Task 4
driver.get(url)
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, search_box)))
print(driver.title)
driver.find_element(By.XPATH, search_box).send_keys("women watch")
driver.find_element(By.XPATH, search_button).click()
verified_header = driver.find_element(By.XPATH, '//h1')
header_text = verified_header.text
print(header_text)
expected_text = "results for women watch"
assert expected_text in header_text
driver.quit()