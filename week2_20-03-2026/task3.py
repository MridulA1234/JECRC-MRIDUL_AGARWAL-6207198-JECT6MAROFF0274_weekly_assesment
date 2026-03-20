from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com")


wait = WebDriverWait(driver, 10)


search = wait.until(EC.presence_of_element_located((By.NAME, "q")))
search.send_keys("Selenium Python")


suggestions = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@role='listbox']//li")))

for s in suggestions:
    print(s.text)


suggestions[0].click()


driver.quit()
