from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/signup")

wait = WebDriverWait(driver, 10)

signup = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='signup-form']")))



signup.find_element(By.NAME, "name").send_keys("Mridul")
signup.find_element(By.NAME, "email").send_keys("mridul@gmail.com")

signup.find_element(By.XPATH, ".//button[text()='Signup']").click()

wait.until(EC.presence_of_element_located((By.ID, "id_gender1"))).click()

newsletter = driver.find_element(By.ID, "newsletter")
offers = driver.find_element(By.ID, "optin")


newsletter.click()
offers.click()


print(newsletter.get_attribute("checked"))
print(offers.get_attribute("checked"))

driver.quit()
