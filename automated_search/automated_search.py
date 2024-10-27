from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=watch&_sacat=0"
rolex_checkbox = '//input[@aria-label="Rolex"]'
casio_checkbox = '//input[@aria-label="Casio"]'
first_rolex_link = '(//ul[@class="srp-results srp-grid clearfix"]//a[@class="s-item__link"]//span[@role="heading"])[1]'
second_rolex_link = '(//ul[@class="srp-results srp-grid clearfix"]//a[@class="s-item__link"]//span[@role="heading"])[2]'
first_rolex_price = '(//ul//span[@class="s-item__price"])[1]'
second_rolex_price = '(//ul//span[@class="s-item__price"])[2]'
expected_text = "rolex"
expected_text_2 = "casio"
last_casio_link = ('(//ul[@class="srp-results srp-grid clearfix"]//a[@class="s-item__link"]//span[@role="heading"])['
                   'last()]')
pre_last_casio_link = ('(//ul[@class="srp-results srp-grid clearfix"]//a[@class="s-item__link"]//span['
                       '@role="heading"])[last()-1]')
mismatches = []

# open main page
driver.get(url)
driver.find_element(By.XPATH, rolex_checkbox).click()
first_listing_text = driver.find_element(By.XPATH, first_rolex_link).text
second_listing_text = driver.find_element(By.XPATH, second_rolex_link).text
if expected_text not in first_listing_text.lower():
    mismatches.append(f'{expected_text} not in {first_listing_text}')
if expected_text not in second_listing_text.lower():
    mismatches.append(f'{expected_text} not in {second_listing_text}')

main_page_first_price = float(driver.find_element(By.XPATH, first_rolex_price).text.replace("$", "").replace(",", ""))
main_page_second_price = float(driver.find_element(By.XPATH, second_rolex_price).text.replace("$", "").replace(",", ""))

first_listing = [first_listing_text, main_page_first_price]
second_listing = [second_listing_text, main_page_second_price]

# open first tab
driver.find_element(By.XPATH, first_rolex_link).click()
driver.switch_to.window(driver.window_handles[1])
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//div[@data-testid="x-item-title"]')))
new_page_first_price = float(driver.find_element(By.XPATH, '//div[@data-testid="x-price-primary"]').text.replace("US $", "").replace(",", ""))
if float(first_listing[1]) != new_page_first_price:
    mismatches.append(f'{float(first_listing[1])} doesn\'t equal {new_page_first_price}')
new_page_first_text = driver.find_element(By.XPATH, '//div[@data-testid="x-item-title"]').text
if first_listing[0] not in new_page_first_text:
    mismatches.append(f'{first_listing[0]} not in {new_page_first_text}')
driver.close()

# open second tab
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH, second_rolex_link).click()
driver.switch_to.window(driver.window_handles[1])
new_page_second_price = float(driver.find_element(By.XPATH, '//div[@data-testid="x-price-primary"]').text.replace("US $", "").replace(",", ""))
if float(second_listing[1]) != new_page_second_price:
    mismatches.append(f'{float(second_listing[1])} doesn\'t equal {new_page_second_price}')
new_page_second_text = driver.find_element(By.XPATH, '//div[@data-testid="x-item-title"]').text
if second_listing[0] not in new_page_second_text:
    mismatches.append(f'{second_listing[0]} not in {new_page_second_text}')
driver.close()

# open main tab
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH, rolex_checkbox).click()
driver.find_element(By.XPATH, casio_checkbox).click()
last_listing_text = driver.find_element(By.XPATH, last_casio_link).text
pre_last_listing_text = driver.find_element(By.XPATH, pre_last_casio_link).text

if expected_text_2 not in last_listing_text.lower():
    mismatches.append(f'{expected_text_2} not in {last_listing_text}')
if expected_text_2 not in pre_last_listing_text.lower():
    mismatches.append(f'{expected_text_2} not in {pre_last_listing_text}')

if mismatches:
    print("Mismatches found")
    for mismatch in mismatches:
        print(mismatch)
else:
    print("No mismatches found.")
