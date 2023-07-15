from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

webdriver_service = Service('c:/Users/meghana/Downloads/chromedriver_win32')
driver = webdriver.Chrome(service=webdriver_service)
driver.get("https://temperaturefinder.web.app/")


temperature_input = driver.find_element(By.ID, "tempe")
temperature_input.clear()
temperature_input.send_keys("Bapatla")
time.sleep(1)
submit_button = driver.find_element(By.ID, "searchBtn")
submit_button.click()
time.sleep(1)
driver.refresh()

temperature_input = driver.find_element(By.ID, "tempe")
temperature_input.clear()
temperature_input.send_keys("Guntur")
time.sleep(1)
submit_button = driver.find_element(By.ID, "searchBtn")
submit_button.click()
time.sleep(1)
driver.refresh()

temperature_input = driver.find_element(By.ID, "tempe")
temperature_input.clear()
temperature_input.send_keys("534341")
time.sleep(1)
submit_button = driver.find_element(By.ID, "searchBtn")
submit_button.click()
time.sleep(1)
driver.refresh()

temperature_input = driver.find_element(By.ID, "tempe")
temperature_input.clear()
temperature_input.send_keys("000000")
time.sleep(1)
submit_button = driver.find_element(By.ID, "searchBtn")
submit_button.click()
time.sleep(1)
driver.refresh()
driver.quit()